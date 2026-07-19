from datetime import datetime
from decimal import Decimal
from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field, field_validator


class EventType(StrEnum):
    TRADE = "TRADE"
    QUOTE = "QUOTE"
    PRICE_UPDATE = "PRICE_UPDATE"


class Exchange(StrEnum):
    NASDAQ = "NASDAQ"
    NYSE = "NYSE"
    ARCA = "ARCA"


class MarketEventCreate(BaseModel):
    model_config = ConfigDict(
        str_strip_whitespace=True,
        json_schema_extra={
            "example": {
                "event_id": "490692a1-bf50-4c87-b0ea-dcde30fd424c",
                "symbol": "AAPL",
                "event_type": "TRADE",
                "price": "192.45",
                "volume": 100,
                "timestamp": "2026-07-19T18:30:00Z",
                "exchange": "NASDAQ",
            }
        },
    )

    event_id: UUID
    symbol: str = Field(min_length=1, max_length=12)
    event_type: EventType
    price: Decimal = Field(gt=0, max_digits=18, decimal_places=6)
    volume: int = Field(gt=0)
    timestamp: datetime
    exchange: Exchange

    @field_validator("symbol")
    @classmethod
    def normalize_symbol(cls, symbol: str) -> str:
        return symbol.upper()

    @field_validator("timestamp")
    @classmethod
    def require_timezone(cls, timestamp: datetime) -> datetime:
        if timestamp.tzinfo is None:
            raise ValueError("timestamp must include a timezone")
        return timestamp

class MarketEventAccepted(BaseModel):
    status: str
    event_id: UUID
    symbol: str
    event_type: EventType