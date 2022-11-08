from unittest import TestCase
import MyAlgorithms

MA = MyAlgorithms


class Test(TestCase):
    def test_insertion_sort(self):
        res = MA.insertion_sort([float], MA.comp)
        self.assertEqual(res, [float])
