from interactors.storage_interfaces.tdr_request_storage_interface import TDRRequestStorageInterface
from mixins.tdr_mixin import TDRMixin
from constants.enum import TDRRequestStatus
from exceptions import tdr_exceptions
from typing import List
from interactors.dtos import TDRRequestDTO


class ReleaseTDRApiInteractor:

    def __init__(self, tdr_request_storage: TDRRequestStorageInterface):
        self.tdr_request_storage = tdr_request_storage

    @property
    def tdr_mixin(self):
        return TDRMixin()

    def release_tdr_api(
            self, tdr_request_id: str,
            user_id: str
    ):
        tdr_requests = self._validate_given_data(
            tdr_request_id=tdr_request_id,
            user_id=user_id
        )

        self.tdr_request_storage.update_tdr_status(
            tdr_request_id=tdr_requests[0].tdr_request_id,
            status=TDRRequestStatus.TDR_RELEASED.value
        )

    def _validate_given_data(
            self, tdr_request_id: str,
            user_id: str
    ) -> List[TDRRequestDTO]:
        tdr_requests = self.tdr_request_storage.get_tdr_requests(
            tdr_request_ids=[tdr_request_id]
        )

        self.tdr_mixin.validate_tdr_request_id(
            tdr_request_id=tdr_requests[0].tdr_request_id,
            tdr_request_storage=self.tdr_request_storage
        )

        entity_id = tdr_requests[0].entity_id
        entity_type = tdr_requests[0].entity_type
        self.tdr_mixin.validate_tdr_entity(
            entity_id=entity_id,
            entity_type=entity_type,
            user_id=user_id
        )

        self._validate_if_current_status_is_pending_certificate_validation(
            tdr_requests=tdr_requests
        )

        return tdr_requests

    @staticmethod
    def _validate_if_current_status_is_pending_certificate_validation(
            tdr_requests: List[TDRRequestDTO]
    ):
        if tdr_requests[0].status != TDRRequestStatus.TDR_CONFIRMED.value:
            raise tdr_exceptions.NotAllowedActionOnTDRRequest(
                tdr_request_id=tdr_requests[0].tdr_request_id,
                current_status=tdr_requests[0].status
            )
