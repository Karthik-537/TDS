from constants.enum import TDRRequestStatus


class InvalidTDRRequestId(Exception):

    def __init__(self, tdr_request_id: str):
        self.tdr_request_id = tdr_request_id

    def __str__(self):
        return f"{self.tdr_request_id}"


class NotAllowedActionOnTDRRequest(Exception):

    def __init__(
            self, tdr_request_id: str,
            current_status: TDRRequestStatus
    ):
        self.tdr_request_id = tdr_request_id
        self.current_status = current_status

    def __str__(self):
        return (f"Action not allowed for TDR request {self.tdr_request_id} in status "
                f"{self.current_status.value}. ")


class InvalidCertificateNumber(Exception):

    def __init__(
            self, certification_number: str
    ):
        self.certification_number = certification_number

    def __str__(self):
        return f"{self.certification_number}"
