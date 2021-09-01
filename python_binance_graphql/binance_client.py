from dataclasses_json.cfg import T
from requests import Session
from hashlib import sha256
from hmac import HMAC

from .models import *
#from .models import CoinInfo, SystemStatus, OldTradeLookup, Snapshot, DepositHistory, SavingsPosition, DepositAddress, AccountStatus
from .utils.binance_request import BinanceGet, BinanceDelete, BinancePost, BinancePut
from .utils.enums import BinanceTransferTypeEnum, BinanceFiatMovementEnum, BinanceFiatPaymentsEnum
from typing import List, Optional, Dict


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

    # WALLET SECTION
    @BinanceGet(path="/sapi/v1/system/status", serialize_to=SystemStatus)
    def get_system_status(self) -> SystemStatus:
        return

    @BinanceGet(signed=True, path="/sapi/v1/capital/config/getall", serialize_to=CoinInfo)
    def get_account_info(self, recvWindow: Optional[int] = None) -> List[CoinInfo]:
        return {"recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/accountSnapshot", signed=True, serialize_to=Snapshot)
    def get_daily_snapshot(self, type: str, startTime: Optional[int] = None, endTime: Optional[int] = None,
                           limit: Optional[int] = None, recvWindow: Optional[int] = None) -> Snapshot:
        return {"type": type, "startTime": startTime, "endTime": endTime, "limit": limit, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/capital/deposit/hisrec", signed=True, serialize_to=DepositHistory)
    def get_deposit_history(self, coin: Optional[str] = None, status: Optional[int] = None, startTime: Optional[int] = None,
                            endTime: Optional[int] = None, offset: Optional[int] = None, limit: Optional[int] = None,
                            recvWindow: Optional[int] = None) -> List[DepositHistory]:
        return {"coin": coin, "status": status, "startTime": startTime, "endTime": endTime, "offset": offset, "limit": limit, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/capital/withdraw/history", signed=True, serialize_to=WithdrawHistory)
    def get_withdraw_history(self, coin: Optional[str] = None, status: Optional[int] = None,
                             withdrawOrderId: Optional[str] = None, offset: Optional[int] = None,
                             limit: Optional[int] = None, startTime: Optional[int] = None,
                             endTime: Optional[int] = None, recvWindow: Optional[int] = None) -> List[WithdrawHistory]:
        return {"coin": coin, "withdrawOrderId": withdrawOrderId, "offset": offset, "limit": limit, "startTime": startTime, "endTime": endTime, "recvWindows": recvWindow}

    @BinanceGet(path="/sapi/v1/capital/deposit/address", signed=True, serialize_to=DepositAddress)
    def get_deposit_address(self, coin: str, network: Optional[str] = None, recvWindow: Optional[int] = None) -> DepositAddress:
        return {"coin": coin, "network": network, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/account/status", signed=True, serialize_to=AccountStatus)
    def get_account_status(self, recvWindow: Optional[int] = None) -> AccountStatus:
        return {"recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/account/apiTradingStatus", signed=True, serialize_to=AccountTradingStatus)
    def get_account_trading_status(self, recvWindow: Optional[int] = None) -> AccountTradingStatus:
        return {"recvWindow": recvWindow}

    @BinanceGet(path="/api/v3/historicalTrades", serialize_to=OldTradeLookup)
    def get_old_trades(self, symbol: str, fromId: Optional[int] = None, limit: Optional[int] = None) -> List[OldTradeLookup]:
        return {"symbol": symbol, "limit": limit, "fromId": fromId}

    @BinanceGet(path="/sapi/v1/asset/dribblet", signed=True, serialize_to=DustLog)
    def get_dust_log(self, startTime: Optional[int] = None, endTime: Optional[int] = None,
                     recvWindow: Optional[int] = None) -> DustLog:
        return {"startTime": startTime, "endTime": endTime, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/asset/assetDividend", signed=True, serialize_to=AssetDividendRecord)
    def get_asset_dividend_record(self, asset: Optional[str] = None, startTime: Optional[int] = None,
                                  endTime: Optional[int] = None, limit: Optional[int] = None,
                                  recvWindow: Optional[int] = None) -> AssetDividendRecord:
        return {"asset": asset, "startTime": startTime, "endTime": endTime, "limit": limit, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/asset/assetDetail", signed=True, serialize_to=AssetDetail)
    def get_asset_detail(self, asset: Optional[str] = None, recvWindow: Optional[int] = None) -> Dict[str, AssetDetail]:
        return {"asset": asset, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/asset/tradeFee", signed=True, serialize_to=TradeFee)
    def get_trade_fee(self, symbol: Optional[str] = None, recvWindow: Optional[int] = None) -> List[TradeFee]:
        return {"symbol": symbol, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/asset/transfer", signed=True, serialize_to=QueryUserUniversalTransferHistory)
    def query_user_universal_transfer_history(self, type: BinanceTransferTypeEnum, startTime: Optional[int] = None,
                                              endTime: Optional[int] = None, current: Optional[int] = None,
                                              size: Optional[int] = None, fromSymbol: Optional[str] = None,
                                              toSymbol: Optional[str] = None, recvWindow: Optional[int] = None
                                              ) -> QueryUserUniversalTransferHistory:

        if (type == BinanceTransferTypeEnum.ISOLATEDMARGIN_ISOLATEDMARGIN or type == BinanceTransferTypeEnum.ISOLATEDMARGIN_MARGIN):
            if not fromSymbol:
                raise(Exception)
        if(type == BinanceTransferTypeEnum.MARGIN_ISOLATEDMARGIN or BinanceTransferTypeEnum.ISOLATEDMARGIN_ISOLATEDMARGIN):
            if not toSymbol:
                raise(Exception)

        return {"type": type.value, "startTime": startTime, "endTime": endTime, "current": current, "size": size,
                "fromSymbol": fromSymbol, "toSymbol": toSymbol, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/account/apiRestrictions", signed=True, serialize_to=APIKeyPermissions)
    def get_api_key_permissions(recvWindow: Optional[int] = None) -> APIKeyPermissions:
        return {"recvWindow": recvWindow}

# SAVINGS SECTION
    @BinanceGet(path="/sapi/v1/lending/daily/token/position", signed=True, serialize_to=SavingsPosition)
    def get_flexible_savings_positions(self, asset: Optional[str] = '', recvWindow: Optional[int] = None) -> List[SavingsPosition]:
        return {"asset": asset, "recvWindow": recvWindow}

# FIAT ENDPOINTS
    @BinanceGet(path="/sapi/v1/fiat/orders", signed=True, serialize_to=FiatHistory)
    def get_fiat_movement_history(self, transactionType: BinanceFiatMovementEnum, beginTime: Optional[int] = None,
                                  endTime: Optional[int] = None, page: Optional[int] = 1, rows: Optional[int] = 100,
                                  recvWindow: Optional[int] = None) -> FiatHistory:
        return {"transactionType": transactionType.value, "beginTime": beginTime, "endTime": endTime, "page": page, "rows": rows, "recvWindow": recvWindow}

    @BinanceGet(path="/sapi/v1/fiat/payments", signed=True, serialize_to=FiatPaymentsHistory)
    def get_fiat_payments_history(self, transactionType: BinanceFiatPaymentsEnum, beginTime: Optional[int] = None,
                                  endTime: Optional[int] = None, page: Optional[int] = 1, rows: Optional[int] = 100,
                                  recvWindow: Optional[int] = None) -> FiatPaymentsHistory:
        return {"transactionType": transactionType.value, "beginTime": beginTime, "endTime": endTime, "page": page, "rows": rows, "recvWindow": recvWindow}
