from unittest import TestCase


class PantryTest(TestCase):
    def setUp(self):
        """Set up with ingredients and recipe for mac_and_cheese and empty pantry"""
        self.pantry = Pantry()

        self.cheese = Ingredient("Cheese", "C", 50)
        self.mac = Ingredient("Macaroni", "oz", 200)

        self.mac_and_cheese = Recipe("Mac and Cheese")
        self.mac_and_cheese.add_ingredient(self.cheese, 2)
        self.mac_and_cheese.add_ingredient(self.mac, 8)

    def test_stock_starts_empty(self):
        """Pantry starts unstocked"""
        self.assertEqual(self.pantry.stock, {})

    def test_you_can_check_stock(self):
        """You can check how much of an ingredient is in the pantry"""
        self.assertEqual(self.pantry.stock_check(self.cheese), 0)

    def test_you_can_restock(self):
        """A stock of ingredients can be added to the pantry"""
        self.pantry.restock(self.cheese, 5)
        self.pantry.restock(self.cheese, 10)

        result = self.pantry.stock_check(self.cheese)

        self.assertEqual(result, 15)

    def test_enough_ingredient_check(self):
        """You can check the pantry to see if you have enough ingredients for a recipe"""
        self.pantry.restock(self.cheese, 5)
        self.pantry.restock(self.cheese, 10)

        self.assertFalse(self.pantry.enough_ingredients_for(self.mac_and_cheese))

        self.pantry.restock(self.mac, 7)
        self.assertFalse(self.pantry.enough_ingredients_for(self.mac_and_cheese))

        self.pantry.restock(self.mac, 1)
        self.assertTrue(self.pantry.enough_ingredients_for(self.mac_and_cheese))
