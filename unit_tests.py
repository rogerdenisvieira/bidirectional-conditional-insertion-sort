import unittest
from sorters import QS, BCIS, IS
import numpy as np
import random

class SortersTestCase(unittest.TestCase):

    def setUp(self):

        self.expected = [0,1,2,3,4,5,6,7,8,9]
        self.non_sorted = [0,1,2,3,4,5,6,7,8,9]
        random.shuffle(self.non_sorted)

        print("Setting things up... Expected: {0} Non-Sorted: {1}".format(self.expected, self.non_sorted))

    
       


    def test_bcis_sorting(self):

        sorter = BCIS()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted)-1)
        self.assertEqual(self.expected, self.non_sorted)

    
    def test_is_sorting(self):
        sorter = IS()
        sorter.sort(self.non_sorted)
        self.assertEqual(self.expected, self.non_sorted)


    def test_qs_sorting(self):
        sorter = QS()
        sorter.sort(self.non_sorted, 0, len(self.non_sorted)-1)
        self.assertEqual(self.expected, self.non_sorted)


    def atest_fake(self):      
        print() 
        self.assertEqual("foo",1)

if __name__ == '__main__':  
    unittest.main()  
