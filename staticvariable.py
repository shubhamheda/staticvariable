from staticexception import StaticNoneTypeException, NonClassException


class staticvariable:
    """
    Static Variable class helps in declaring the static variable within the class
    Method:
        staticvariable(class_name, variable_name, variable_value)

    """

    def __init__(self, class_name, variable_name, variable_value):
        if class_name is None:
            raise StaticNoneTypeException
        else:
            self.class_name = str(class_name.__name__) + "Static"
            self.variable_name = '__' + variable_name
            self.initialize(class_name, variable_value)

    def initialize(self, class_name, variable_value):
        if type(class_name) is type:
            if self.class_name not in globals().keys():
                globals()[self.class_name] = {}
                globals()[self.class_name]['__staticvariable'] = {self.variable_name: variable_value}
            else:
                if self.variable_name not in globals()[self.class_name]['__staticvariable'].keys():
                    globals()[self.class_name]['__staticvariable'] = {self.variable_name: variable_value}
        else:
            raise NonClassException

    def get_static_value(self, variable_name):
        """ Get value of static variable in python """
        if self.variable_name == '__' + variable_name:
            return globals()[self.class_name]['__staticvariable'][self.variable_name]
        else:
            raise AttributeError("Attribute Not Found")

    def set_static_value(self, variable_name, variable_value):
        """ Set value of static variable"""
        if self.variable_name == '__' + variable_name:
            return globals()[self.class_name]['__staticvariable'].update({self.variable_name: variable_value})
        else:
            raise AttributeError("Attribute Not Found")
