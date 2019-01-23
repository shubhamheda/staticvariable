from staticvariable import staticvariable


class DemoClassStaticVariable:
    def __init__(self):
        self.value = staticvariable(DemoClassStaticVariable, "value", 100)

    def get_value(self):
        return self.value.get_static_value("value")

    def set_value(self, value):
        self.value.set_static_value("value", value)
