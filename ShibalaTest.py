import unittest
from Shibala import Shibala
from Player import Player
from random import randrange



class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.shibala = Shibala()

    def tearDown(self):
        self.shibala = None

    def test_is_ise(self):
        dice=[1,1,1,1]
        self.assertTrue(self.shibala._isISe(dice), "Should be i-se")

    def test_illegal_ise(self):
        dice=[1,2,3,4]
        self.assertFalse(self.shibala._isISe(dice), "Should not be i-se")

    def test_is_shibala(self):
        dice=[1,1,6,6]
        self.assertTrue(self.shibala._isShiBa(dice), "Should be shibala")

    def test_count_score_with_two_pair(self):
        dice=[1,1, 5, 5]
        self.assertEqual(10, self.shibala._score(dice), "Incorrect Number")

    def test_count_score_with_one_pair(self):
        dice=[1,2, 5, 5]
        self.assertEqual(3, self.shibala._score(dice), "Incorrect Number")

    def test_count_score_with_no_pair(self):
        dice=[1,2, 3, 5]
        self.assertEqual(0, self.shibala._score(dice), "Incorrect Number")

    def test_illegal_shibala(self):
        dice=[1,3,4,4]
        self.assertFalse(self.shibala._isShiBa(dice), "Should not be shibala")

    def test_legal_number_after_roll(self):
        self.shibala.roll(Player("A"), Player("B"))
        for i in self.shibala.dice_one:
            self.assertTrue(0 < i < 7, "Illegal Number")
        for i in self.shibala.dice_two:
            self.assertTrue(0 < i < 7, "Illegal Number")

if __name__ == '__main__':
    unittest.main()
