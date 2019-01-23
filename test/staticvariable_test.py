import unittest
from DemoClassStaticVariable import DemoClassStaticVariable


class staticvariable_test(unittest.TestCase):

    def setUp(self):
        self.d = DemoClassStaticVariable()
        self.d1 = DemoClassStaticVariable()

    def test_value_in_remains_same_for_different_objects(self):
        self.assertEqual(self.d.value.get_static_value("value"), 100)
        # Change value from d and get same value from d1 object
        self.d.value.set_static_value("value", 2000)
        self.assertEqual(self.d1.value.get_static_value("value"))
