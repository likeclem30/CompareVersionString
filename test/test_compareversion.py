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

    def test_compareVersion_different_length_Equal_version_case01(self):
        """ Compare version1 = '1.1.0' and version2 = '1.1'. it should return 0. The Two versions are equal \n """
        self.version1 = '1.1.0'
        self.version2 = '1.1'
        self.assertEqual(cv.compareVersion(self.version1, self.version2),0)
        print("\n In test_compareVersion_different_length_Equal_version_case01()")
     
    def test_compareVersion_Same_length_Equal_version_case02(self):
        """ Compare version1 = '1.1.0' and version2 = '1.1.0'. it should return 0. The Two versions are equal \n """
        self.version1 = '1.1.0'
        self.version2 = '1.1.0'
        self.assertEqual(cv.compareVersion(self.version1, self.version2),0)
        print("\n In test_compareVersion_Same_length_Equal_version_case02()")

    def test_compareVersion_different_length_first_bigger_version_case01(self):
        """ Compare version1 = '1.0.1' and version2 = '1'. it should return 1. Versions2 is smaller \n """
        self.version1 = '1.1.0'
        self.version2 = '1'
        self.assertEqual(cv.compareVersion(self.version1, self.version2),1)
        print("\n In test_compareVersion_different_length_first_bigger_version_case01()")
     
    def test_compareVersion_same_length_first_bigger_version_case02(self):
        """ Compare version1 = '2.0.1' and version2 = '2.0.0'. it should return 1. Versions2 is smaller \n """
        self.version1 = '2.0.1'
        self.version2 = '2.0.0'
        self.assertEqual(cv.compareVersion(self.version1, self.version2),1)
        print("\n In test_compareVersion_same_length_first_bigger_version_case02()")

    def test_compareVersion_different_length_second_bigger_version_case01(self):
        """ Compare version1 = '1.1.0' and version2 = '1.1.1.3.0.0'. it should return -1. Versions1 is Smaller \n """
        self.version1 = '1.1.0'
        self.version2 = '1.1.1.3.0.0'
        self.assertEqual(cv.compareVersion(self.version1, self.version2),-1)
        print("\n In test_compareVersion_different_length_second_bigger_version_case01()")

    def test_compareVersion_same_length_second_bigger_version_case02(self):
        """ Compare version1 = '1.1.0.3.0.0' and version2 = '1.1.1.3.0.0'. it should return -1. Versions1 is Smaller \n """
        self.version1 = '1.1.0.3.0.0'
        self.version2 = '1.1.1.3.0.0'
        self.assertEqual(cv.compareVersion(self.version1, self.version2),-1)
        print("\n In test_compareVersion_same_length_second_bigger_version_case02()")   
