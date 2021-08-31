from requests import Session
from hashlib import sha256
from hmac import HMAC

from .models import CoinInfo, SystemStatus, OldTradeLookup, Snapshot, DepositHistory, SavingsPosition
from .utils.binance_request import BinanceGet, BinanceDelete, BinancePost, BinancePut
from typing import List, Optional


class BinanceClient:
    def __init__(self, api_key: str, secret: str, base_uri: str = "https://api.binance.com"):
        self.base_uri = base_uri
        self.secret = secret
        self.api_key = api_key.encode("utf-8")

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
    def get_account_info(self, recvWindow: Optional[int] = None) -> List[CoinInfo]:
        return {"recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/system/status", serialize_to=SystemStatus)
    def get_system_status(self) -> SystemStatus:
        return

    @BinanceGet(path="/api/v3/historicalTrades", serialize_to=OldTradeLookup)
    def get_old_trades(self, symbol: str, fromId: Optional[int] = None, limit: Optional[int] = None) -> List[OldTradeLookup]:
        return {"symbol": symbol, "limit": limit, "fromId": fromId}

    @BinanceGet(path="/sapi/v1/accountSnapshot", signed=True, serialize_to=Snapshot)
    def get_daily_snapshot(self, type: str, startTime: Optional[int] = None, endTime: Optional[int] = None,
                           limit: Optional[int] = None, recvWindow: Optional[int] = None) -> Snapshot:
        return {"type": type, "startTime": startTime, "endTime": endTime, "limit": limit, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/capital/deposit/hisrec", signed=True, serialize_to=DepositHistory)
    def get_deposit_history(self, coin: Optional[str] = None, status: Optional[int] = None, startTime: Optional[int] = None,
                            endTime: Optional[int] = None, offset: Optional[int] = None, limit: Optional[int] = None,
                            recvWindow: Optional[int] = None) -> List[DepositHistory]:
        return {"coin": coin, "status": status, "startTime": startTime, "endTime": endTime, "offset": offset, "limit": limit, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/lending/daily/token/position", signed=True, serialize_to=SavingsPosition)
    def get_flexible_savings_positions(self, asset: Optional[str] = '', recvWindow: Optional[int] = None) -> List[SavingsPosition]:
        return {"asset": asset, "recvWindow": recvWindow}
