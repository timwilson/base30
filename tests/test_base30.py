import unittest
from base30.base30 import dec_to_b30, b30_to_dec

class TestConvertToBase30(unittest.TestCase):

    def test_convert_base_name(self):
        self.assertEqual(dec_to_b30(30), "10")
    
    def test_convert_large_num(self):
        self.assertEqual(dec_to_b30(20210504), "SXJ3G")


class TestConvertToDecimal(unittest.TestCase):

    def test_convert_base_num(self):
        self.assertEqual(b30_to_dec("10"), 30)
    
    def test_convert_large_num(self):
        self.assertEqual(b30_to_dec("SXJ3G"), 20210504)


if __name__ == '__main__':
    unittest.main()
