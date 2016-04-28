"""
Unit tests

"""
import unittest

from giog import ogham


class TestOgham(unittest.TestCase):

    def test_ogham(self):
        input_str = 'Dia duit, a Dhomhain.'

        ogham_str = ogham.ogham(input_str)

        self.assertEqual(ogham_str, '᚛ᚇᚔᚐ ᚇᚗᚈ ᚐ ᚇᚆᚑᚋᚆᚐᚔᚅ᚜')
