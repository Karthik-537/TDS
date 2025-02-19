from dataclasses import dataclass
from constants.enum import (
    TDREntityType,
    TDRRequestStatus,
    TDRRequestAPILogStatus
)
from typing import Optional
from datetime import datetime


@dataclass
class TDRRequestDTO:
    tdt_request_id: str
    entity_id: str
    entity_type: TDREntityType
    certificate_number: str
    requested_area: str
    market_value_for_requested_area: float
    market_value_for_usage_area: Optional[float]
    status: TDRRequestStatus
    issued_datetime: Optional[datetime]


@dataclass
class TDRRequestAPILogDTO:
    tdr_request_id: str
    request: str
    response: str
    requested_at: datetime
    status: TDRRequestAPILogStatus
    traceback: str


@dataclass
class CreateTDRRequestParamsDTO:
    certificate_number: str
    requested_area: str
    market_value_for_requested_area: float
    entity_id: str
    entity_type: TDREntityType
    user_id: str

