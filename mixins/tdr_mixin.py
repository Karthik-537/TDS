from interactors.storage_interfaces.storage_interface import StorageInterface
from constants.enum import TDREntityType
from exceptions import tdr_exceptions


class TDRMixin:

    def validate_tdr_entity(
            self,
            entity_id: str,
            entity_type: TDREntityType,
            user_id: str
    ):
        raise NotImplementedError()
