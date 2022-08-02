class ApiException(Exception):
    """Handle all custom API exceptions"""
    pass

class BadRequestException(ApiException):
    """Bad request exception"""
    code = 400
    error = "Bad request"
