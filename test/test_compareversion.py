import unittest
from comparevs import compareVersionString as cv

class TestCase01(unittest.TestCase):
    def test_padStringZero01(self):
        """ if version 1 is '1.0.1' and version2 = '1' make or reformat version2 to '1.0.0' before invoking the compareversion function\n """
        self.version = '1'
        self.version = self.version.split('.')
        self.length = 3
        self.padding = '0'
        self.assertCountEqual(cv.padStringZero(self.version, self.length, self.padding),['1', '0', '0'])
        print("\n In test_padStringZero01()")
       

    def test_padStringZero02(self):
        """ if version 1 is '1.1' and version2 = '1' make or reformat version2 to '1.0' before invoking the compareversion function\n """
        self.version = '1'
        self.version = self.version.split('.')
        self.length = 2
        self.padding = '0'
        self.assertCountEqual(cv.padStringZero(self.version, self.length, self.padding),['1', '0'])
        print("\n In test_padStringZero02()")
        
