

import unittest
from functions import get_full_name

class checkfunc_test(unittest.TestCase):
    def test_func(self):
        name = get_full_name("dua", "lipa")
        self.assertEqual(name, "Dua Lipa")
    
    def test_familyname(self):
        name = get_full_name("dua", "lipa", "brain")
        self.assertEqual(name, "Dua Lipa Brain")

unittest.main()