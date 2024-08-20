from rest_framework.exceptions import APIException

class AlreadyExistsException(APIException):
    status_code = 409
    default_detail = "A user with this email already exists."
    default_code = "user_already_exists"

class ServiceUnavailableException(APIException):
    status_code = 503
    default_detail = "The service is currently unavailable."
    default_code = "service_unavailable"
