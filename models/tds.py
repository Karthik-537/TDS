from django.db import models
import uuid


def _generate_uuid4_str():
    return str(uuid.uuid4())


def validate_tdr_entity_type(value: str):
    from constants.enum import TDREntityType

    if value not in TDREntityType.get_list_of_values():
        raise Exception(f"Invalid_entity_type: {value}")


def validate_tdr_request_status(value: str):
    from constants.enum import TDRRequestStatus

    if value not in TDRRequestStatus.get_list_of_values():
        raise Exception(f"Invalid_tdr_request_status: {value}")


def validate_tdr_request_api_log_status(value: str):
    from constants.enum import TDRRequestAPILogStatus

    if value not in TDRRequestAPILogStatus.get_list_of_values():
        raise Exception(f"Invalid_tdr_request_api_log_status: {value}")


class TDRRequest(models.Model):
    tdr_request_id = models.CharField(
        max_length=255, primary_key=True, default=_generate_uuid4_str()
    )
    entity_id = models.CharField(max_length=255)
    entity_type = models.CharField(
        max_length=255, validators=[validate_tdr_entity_type]
    )
    requested_area = models.CharField(max_length=255)
    market_value_for_requested_area = models.FloatField()
    market_value_for_usage_area = models.FloatField(null=True, blank=True)
    status = models.CharField(
        max_length=255, validators=[validate_tdr_request_status]
    )
    issued_datetime = models.DateTimeField(null=True, blank=True)


class TDRRequestAPILog(models.Model):
    tdr_request_id = models.CharField(
        max_length=255, primary_key=True, default=_generate_uuid4_str()
    )
    request = models.TextField()
    response = models.TextField()
    requested_at = models.DateTimeField()
    status = models.CharField(
        max_length=255, validators=[validate_tdr_request_api_log_status]
    )
    traceback = models.TextField()

