import unittest
from unittest.mock import patch
from ex_1 import p_number
import io
from collections.abc import MutableMapping


class TestPyramidalNumber(unittest.TestCase):
    
    def test_p_number_with_positive_input(self):
        self.assertEqual(p_number(1), 1) 
        # self.assertEqual(p_number(2), 4)  
        self.assertEqual(p_number(3), 10)  


    def test_p_number_with_zero_input(self):
        self.assertEqual(p_number(0), 0)  

    def test_p_number_with_negative_input(self):
        self.assertEqual(p_number(-1), 0)  

if __name__ == '__main__':
    import collections.abc
    import collections
    collections.MutableMapping = collections.abc.MutableMapping
    from xmlrunner import XMLTestRunner

    
    runner = XMLTestRunner(output='test-reports')
    unittest.main(testRunner=runner)
    unittest.main()