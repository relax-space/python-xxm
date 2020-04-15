import unittest
from newer import level1

"""
py.test.exe tests/level1_test.py -s
"""

class TestLevel1(unittest.TestCase):

    def testStrDto(self):
        print(1)
        dto = level1.StrDto()
        value = dto.getString()
        expUp = value.upper()
        actUp = dto.printString(value)
        self.assertEqual(actUp,expUp)


        

        
    


        


        