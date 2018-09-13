import unittest
from bank import Bank


class test_bank(unittest.TestCase):

    def test_balance_not_enought_money(self):
        bank = Bank("Milena", 300)
        result = bank.take_out_money(500)
        self.assertEqual(result,"Mr/Mrs Milena don´t have enought money in your account")

    def test_balance_enought_money(self):
        bank = Bank("Milena", 1500)
        result = bank.take_out_money(500)
        self.assertEqual(result,"Succesful transaction")


