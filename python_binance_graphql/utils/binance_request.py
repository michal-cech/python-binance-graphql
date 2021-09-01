from hashlib import sha256
from functools import wraps
import time
from datetime import datetime
import hmac

import requests
from requests.models import Response


class BinanceRequest:
    def __init__(self, method, path, signed=False, serialize_to=None):
        self.method = method.upper()
        self.path = path
        self.signed = signed
        self.serialize_to = serialize_to

    @staticmethod
    def get_query_string(params):
        query_string = "&"
        query_params = []

        for k, v in params.items():
            if v is None:
                continue
            if isinstance(v, list):
                query_params += [f"{k}={val}" for val in v]
            else:
                query_params.append(f"{k}={v}")
        query_string = query_string.join(query_params)
        return query_string

    @staticmethod
    def _handle_error(response: Response):
        print(
            f"Error! Status Code{response.status_code}, reason: {response.text}")
        raise (Exception)

    @staticmethod
    def _get_timestamp():
        return int(datetime.now().timestamp() * 1000)

    @staticmethod
    def _serialize_response(response: dict, cls):
        if isinstance(response, list):
            return [cls.from_dict(obj) for obj in response]
        return cls.from_dict(response)

    def __call__(self, func):
        @wraps(func)
        def wrapper(obj, *args, **kwargs):
            payload = func(obj, *args, **kwargs)
            request_args = {
                'url': f"{obj.base_uri}{self.path}",
                'method': self.method,
            }

            if self.signed:
                if not payload:
                    payload = {}

                payload.update(
                    {"timestamp": self._get_timestamp()})
                query_string = self.get_query_string(payload)
                payload.update({"signature": hmac.new(
                    obj.secret.encode("utf-8"), query_string.encode("utf-8"), digestmod=sha256).hexdigest()})

            request_args['params'] = payload

            request = requests.Request(**request_args)
            prepared = obj.session.prepare_request(request)
            response = obj.session.send(prepared)

            if response.status_code < 200 or response.status_code > 300:
                self._handle_error(response)

            result = response.json()
            if self.serialize_to:
                result = self._serialize_response(result, self.serialize_to)
            return result
        return wrapper


class BinanceGet(BinanceRequest):
    def __init__(self, path, signed=False, serialize_to=None):
        super().__init__(method='GET', path=path, signed=signed, serialize_to=serialize_to)


class BinancePost(BinanceRequest):
    def __init__(self, path, signed=False, serialize_to=None):
        super().__init__(method='POST', path=path, signed=signed, serialize_to=serialize_to)


class BinancePut(BinanceRequest):
    def __init__(self, path, signed=False, serialize_to=None):
        super().__init__(method='PUT', path=path, signed=signed, serialize_to=serialize_to)


class BinanceDelete(BinanceRequest):
    def __init__(self, path, signed=False, serialize_to=None):
        super().__init__(method='DELETE', path=path,
                         signed=signed, serialize_to=serialize_to)
