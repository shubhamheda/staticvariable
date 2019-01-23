class StaticNoneTypeException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "Static Variable cannot be NoneType"
        if "message" in kwargs.keys():
            self.message = kwargs.get("message")
        super(StaticNoneTypeException, self).__init__(self.message)


class NonClassException(Exception):
    def __init__(self, *args, **kwargs):
        self.message = "Class Name given is not a class"
        if "message" in kwargs.keys():
            self.message = kwargs.get("message")
        super(NonClassException, self).__init__(self.message)
