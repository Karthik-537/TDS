from interactors.dtos import TDRRequestDTO
from typing import List
from constants.enum import TDRRequestStatus


class TDRRequestStorageInterface:

    def create_tdr_request(
            self, tdr_request_dto: TDRRequestDTO
    ) -> TDRRequestDTO:
        pass

    def get_valid_tdr_request_ids(
            self, tdr_request_ids: List[str]
    ) -> List[str]:
        pass

    def get_tdr_requests(
            self, tdr_request_ids: List[str]
    ) -> List[TDRRequestDTO]:
        pass

    def update_tdr_status(
            self, tdr_request_id: str,
            status: TDRRequestStatus
    ):
        pass
