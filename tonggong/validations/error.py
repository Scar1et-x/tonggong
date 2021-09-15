class BaseValidationError(Exception):
    def __init__(self, message=None, data=None):
        if not isinstance(message, str):
            message = f"{message}"
        self.message = message
        self.data = data

    def __str__(self):
        return f"{type(self)}: {self.message}"


class ParamError(BaseValidationError):
    def __init__(self, message=None):
        super(ParamError, self).__init__(message=message)


class MinLengthError(BaseValidationError):
    def __init__(self, message=None):
        super(MinLengthError, self).__init__(message=message)


class MaxLengthError(BaseValidationError):
    def __init__(self, message=None):
        super(MaxLengthError, self).__init__(message=message)


class NullError(BaseValidationError):
    def __init__(self, message=None):
        super(NullError, self).__init__(message=message)


class LengthError(BaseValidationError):
    def __init__(self, message=None):
        super(LengthError, self).__init__(message=message)


class EmailError(BaseValidationError):
    def __init__(self, message=None):
        super(EmailError, self).__init__(message=message)


class SchemaError(BaseValidationError):
    def __init__(self, message=None, data=None):
        super(SchemaError, self).__init__(message=message, data=data)
