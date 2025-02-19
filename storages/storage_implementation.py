from interactors.dtos import TDRRequestDTO
from interactors.storage_interfaces.storage_interface import StorageInterface
from models.tds import TDRRequest


class StorageImplementation(StorageInterface):

    def create_tdr_request(
            self, tdr_request_dto: TDRRequestDTO
    ) -> TDRRequestDTO:
        pass


