from interactors.storage_interfaces.tdr_request_storage_interface import TDRRequestStorageInterface
from constants.enum import (
    TDREntityType,
    TDRRequestStatus
)
from exceptions import tdr_exceptions


class TDRMixin:

    def validate_tdr_entity(
            self,
            entity_id: str,
            entity_type: TDREntityType,
            user_id: str
    ):
        raise NotImplementedError()

    @staticmethod
    def validate_tdr_request_id(
            tdr_request_id: str,
            tdr_request_storage: TDRRequestStorageInterface
    ):
        valid_ids = tdr_request_storage.get_valid_tdr_request_ids(
            tdr_request_ids=[tdr_request_id]
        )
        if tdr_request_id not in valid_ids:
            raise tdr_exceptions.InvalidTDRRequestId(
                tdr_request_id=tdr_request_id
            )
