from interactors.dtos import TDRRequestDTO


class StorageInterface:

    def create_tdr_request(
            self, tdr_request_dto: TDRRequestDTO
    ) -> TDRRequestDTO:
        pass
