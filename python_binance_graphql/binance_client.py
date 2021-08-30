from requests import Session
from hashlib import sha256
from hmac import HMAC

from .models import CoinInfo, SystemStatus
from .utils.binance_request import BinanceGet, BinanceDelete, BinancePost, BinancePut


class BinanceClient:
    def __init__(self, api_key, secret, base_uri="https://api.binance.com"):
        self.base_uri = base_uri
        self.secret = secret
        self.api_key = api_key

        # prepare session
        session = Session()
        session.headers = {
            "Content-Type": "application/json;charset=utf-8",
            "User-Agent": "investing-dashboard",
            "X-MBX-APIKEY": self.api_key,
        }
        self.session = session

    @property
    def session(self) -> Session:
        return self._session

    @session.setter
    def session(self, value) -> Session:
        self._session = value

    def _get_signature(self, data):
        return HMAC(self.secret, data, digestmod=sha256).hexdigest()

    @BinanceGet(signed=True, path="/sapi/v1/capital/config/getall", serialize_to=CoinInfo)
    def get_account_info(self) -> CoinInfo:
        return {"recvWindow": 10000}

    @BinanceGet(path="/sapi/v1/system/status", serialize_to=SystemStatus)
    def get_system_status(self) -> SystemStatus:
        return
