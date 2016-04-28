"""
Unit tests

"""
import unittest

from giog import ogham


class TestOgham(unittest.TestCase):

    def test_normalise(self):
        ga_str = 'dia duit'
        en_str = 'xylophone'  # x and y are not valid characters

        ga_norm = ogham.normalise(ga_str)
        en_norm = ogham.normalise(en_str)

        self.assertEqual(ga_str, ga_norm)
        self.assertNotEqual(en_str, en_norm)


    def test_ogham(self):
        input_str = 'Dia duit, a Dhomhain.'

        ogham_str = ogham.ogham(input_str)

        self.assertEqual(ogham_str, '᚛ᚇᚔᚐ ᚇᚗᚈ ᚐ ᚇᚆᚑᚋᚆᚐᚔᚅ᚜')
