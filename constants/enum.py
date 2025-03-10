from enum import Enum


class TDRRequestStatus(Enum):
    PENDING_CERTIFICATE_VALIDATION = "PENDING_CERTIFICATE_VALIDATION"
    CERTIFICATE_VALIDATED = "CERTIFICATE_VALIDATED"
    CERTIFICATE_OWNERSHIP_VERIFIED = "CERTIFICATE_OWNERSHIP_VERIFIED"
    TDR_INITIATED = "TDR_INITIATED"
    TDR_RELEASED = "TDR_RELEASED"
    TDR_CONFIRMED = "TDR_CONFIRMED"


class TDREntityType(Enum):
    PIPELINE_ITEM = "PIPELINE_ITEM"


class TDRRequestAPILogStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILURE = "FAILURE"

