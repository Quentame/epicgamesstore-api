class EGSException(Exception):
    """
    Class for EGS errors, all data about error is placed in ``exception_data``
    """
    def __init__(self, message, error_code=None, service_response=None):
        super(EGSException, self).__init__(message)
        self.message = (
            f'Error code: '
            f'{error_code if error_code is not None else "unknown"}. '
            f'{message.capitalize()}'
        )
        self.exception_data = service_response

    def __str__(self):
        return self.message


class EGSNotFound(EGSException):
    """
    All errors which error code ends with `not_found`
    """
    pass
