from interactors.dtos import TDRRequestDTO
from interactors.storage_interfaces.tdr_request_storage_interface import TDRRequestStorageInterface
from models.tds import TDRRequest


class TDRequestStorageImplementation(TDRRequestStorageInterface):

    def create_tdr_request(
            self, tdr_request_dto: TDRRequestDTO
    ) -> TDRRequestDTO:
        pass


