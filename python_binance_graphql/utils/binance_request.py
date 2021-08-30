from hashlib import sha256
from functools import wraps
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
        query_string = "&".join(f"{k}={v}" for k, v in params.items())
        return query_string

    @staticmethod
    def _handle_error(response: Response):
        print(
            f"Error! Status Code{response.status_code}, reason: {response.text}")
        raise (Exception)

    def __call__(self, func):
        def wrapper(obj, *args, **kwargs):
            payload = func(obj, *args, **kwargs)
            request_args = {
                'url': f"{obj.base_uri}{self.path}",
                'method': self.method,
                'json': {}
            }
            if payload:
                request_args['json'] = payload

            if self.signed:
                payload["json"].update(
                    {"timestamp": datetime.timestamp(datetime.now())})
                query_string = self.get_query_string(payload)
                request_args["json"].update({"signature": hmac.new(
                    obj.secret.encode("utf-8"), query_string.encode("utf-8"), digestmod=sha256).hexdigest()})

            request = requests.Request(**request_args)
            prepared = obj.session.prepare_request(request)
            response = obj.session.send(prepared)

            if not ((self.method == 'GET' and response.status_code == 200) or
                    (response.status_code == 201)):
                self._handle_error(response)
            result = response.json()
            if self.serialize_to:
                result = self.serialize_to.from_dict(result)
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
