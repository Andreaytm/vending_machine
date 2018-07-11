import unittest
from vending_machine import give_change, give_item_and_change


class TestVendingMachine(unittest.TestCase):
    def test_return_change(self):
        self.assertEqual(give_change(.17), [.10, .05, .02])
        self.assertEqual(give_change(.18), [.10, .05, .02, .01])
        self.assertEqual(give_change(.04), [.02, .02])

    def test_multiple_same_coins(self):
        """ machine accepts multiples of same coin"""
        self.assertEqual(give_change(.40), [.20, .20])

    def test_unavailable_item(self):
        """if user asks for an item that's unavailable, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('crisps', .50)
        self.assertIsNone(item)
        self.assertEqual(change, .50)

    def test_not_enough_money(self):
        """if user does not provide enough money to buy item, they should not be given the item, and their money should be returned"""
        item, change, _ = give_item_and_change('coke', .50)
        self.assertIsNone(item)
        self.assertEqual(change, .50)

    def test_correct_change(self):
        """if user asks for an item and pays too much
        they should get the correct change

        item, change, _ = give_item_and_change('coke', 1.00)
        self.assertEqual(change, [.20, .05, .02]) """
        item, change, _ = give_item_and_change('coke', 1.00)
        self.assertEqual(change, [.20, .05, .02])

    """ 
    def test_no_change(self):
        NOTE:CHALLENGE = EVIL =if user puts in too much money, machine returns item but gives no change 
        -  in scenario would change vending_machine.py "change_to_return = 0" therefore no coins returned.
        item, change, _ = give_item_and_change('biscuits', [.50, 1])
        self.assertEqual(change, [])      """


    """def test_return_some_change(self):
        Note: CHALLENGE = EVIL if user puts in money, machine will return some change and item
        - in scenariou would change vending_machine py "change_to_return = (amount - cost) / 2" 
        therefore fewer coins than actual change is returned in case below apple cost = .43 
        amount paid is 1, actual change should be .57, but instead difference is .285 meaning 28p is returned.
        The amount returned is at the whole number and not rounded.
        
        item, change, _ = give_item_and_change('apple', 1.00)
        self.assertEqual(change, [.20, .05, .02, .01])"""