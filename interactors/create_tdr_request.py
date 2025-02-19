from interactors.storage_interfaces.storage_interface import StorageInterface
from interactors.dtos import (
    CreateTDRRequestParamsDTO,
    TDRRequestDTO
)
from exceptions import tdr_exceptions
from mixins.tdr_mixin import TDRMixin
import uuid
from constants.enum import TDRRequestStatus


def _generate_uuid4_str():
    return str(uuid.uuid4())


class CreateTDRRequestInteractor(TDRMixin):
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    @property
    def tdr_mixin(self):
        return TDRMixin()

    def create_tdr_request(self, params_dto: CreateTDRRequestParamsDTO):
        self.tdr_mixin.validate_tdr_entity(
            entity_id=params_dto.entity_id,
            entity_type=params_dto.entity_type,
            user_id=params_dto.user_id
        )
        tdr_request_dto = TDRRequestDTO(
            tdt_request_id=_generate_uuid4_str(),
            entity_id=params_dto.entity_id,
            entity_type=params_dto.entity_type,
            certificate_number=params_dto.certificate_number,
            requested_area=params_dto.requested_area,
            market_value_for_requested_area=params_dto.market_value_for_requested_area,
            status=TDRRequestStatus.PENDING_CERTIFICATE_VALIDATION.value,
            market_value_for_usage_area=None,
            issued_datetime=None
        )
        self.storage.create_tdr_request(
            tdr_request_dto=tdr_request_dto
        )
