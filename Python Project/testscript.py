import unittest
import random
from pythonmain import *

class TestStringMethods(unittest.TestCase):

    def test_flatten(self):
        empty_array = []
        self.assertEqual(flatten([6,2,[4,3],[[[5],None],1]], empty_array) , [6, 2, 4, 3, 5, None, 1])
        empty_array = []
        self.assertEqual(flatten([1], empty_array) , [1])
        empty_array = []
        self.assertEqual(flatten([[[[[[[[1,2]]],3]]]],4], empty_array) , [1,2,3,4])
        empty_array = []
        self.assertEqual(flatten([[[[]]]], empty_array) , [])
        
    def test_removeNull(self):
        self.assertEqual(removeNone([1,None, None, 3, 1]),[1,3,1])
        self.assertEqual(removeNone([None,None, None, None, None]),[])

    def test_numberOfElements(self):
        n = 10001   # Choose an array size
        array_test = [random.random() for _ in range(n)]
        self.assertNotEqual(numOfElements(array_test),True, "Cannot not sort an array greater than 10000 elements")

    def test_bubblesort(self):
        self.assertEqual(bubbleSort([6,2,[4,3],[[[5],None],1]]),[1, 2, 3, 4, 5, 6])
        
if __name__ == '__main__':
   # unittest.main()
   suite = unittest.TestSuite()
   suite.addTests([TestStringMethods('test_numberOfElements'),TestStringMethods('test_flatten'),TestStringMethods('test_removeNull'),TestStringMethods('test_bubblesort')])
   result = unittest.TextTestRunner(verbosity=2).run(suite)

   if result.wasSuccessful():
       exit(0)
   else:
       exit(1)
