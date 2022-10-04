class OpenaqApiException(Exception):
    """
        Class to handle the OpenAQ API Exceptions. Inherits from Exception base class.
    """
    def __init__(self, response, request):
        """
            Initialization of the class given a response and a request
        :param response: Response of the call to the API
        :param request:  Request made to the API
        """
        if response.status_code == 429:
            raise CallLimit("Call limit exceeded. Temporary block.", request)
        elif response.status_code == 422:
            raise Validation("Validation error in the request", request)
        elif response.status_code == 500:
            raise InternalServer("Internal server error", request)
        elif response.status_code == 100:
            raise MissingParam("Parameter error in the request", request)
        else:
            raise UnknownException("Unknown exception occurred.", request)


class CallLimit(Exception):
    def __init__(self, message, request):
        super().__init__({'message': message, 'request': request})


class Validation(Exception):
    def __init__(self, message, request):
        super().__init__({'message': message, 'request': request})


class InternalServer(Exception):
    def __init__(self, message, request):
        super().__init__({'message': message, 'request': request})


class MissingParam(Exception):
    def __init__(self, message, request):
        super().__init__({'message': message, 'request': request})


class UnknownException(Exception):
    def __init__(self, message, request):
        super().__init__({'message': message, 'request': request})
