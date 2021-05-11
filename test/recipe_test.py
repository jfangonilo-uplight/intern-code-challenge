from unittest import TestCase


class RecipeTest(TestCase):
    def setUp(self):
        """Set up with ingredients and recipe for mac_and_cheese"""
        self.cheese = Ingredient("Cheese", "C", 100)
        self.mac = Ingredient("Macaroni", "oz", 30)

        self.mac_and_cheese = Recipe("Mac and Cheese")

    def test_it_exists(self):
        """mac_and_cheese is a Recipe instance"""
        self.assertIsInstance(self.mac_and_cheese, Recipe)

    def test_it_has_a_name(self):
        """mac_and_cheese object has a name"""
        self.assertEqual(self.mac_and_cheese.name, "Mac and Cheese")

    def test_you_can_add_ingredients(self):
        """mac_and_cheese object instantiates with no ingredients, but can be added"""
        self.assertEqual(self.mac_and_cheese.ingredients_required, {})

        self.mac_and_cheese.add_ingredient(self.cheese, 2)
        self.mac_and_cheese.add_ingredient(self.mac, 8)

        expected = {
            self.cheese: 2,
            self.mac: 8
        }

        self.assertEqual(self.mac_and_cheese.ingredients_required, expected)

    def test_you_can_get_amounts(self):
        """You can get the amount of ingredients in a recipe"""
        self.mac_and_cheese.add_ingredient(self.cheese, 2)
        self.mac_and_cheese.add_ingredient(self.mac, 8)

        cheese_required = self.mac_and_cheese.amount_required(self.cheese)
        mac_required = self.mac_and_cheese.amount_required(self.mac)

        self.assertEqual(cheese_required, 2)
        self.assertEqual(mac_required, 8)

    def test_you_can_get_list_of_ingredients(self):
        """You can get list of ingredients in a recipe"""
        self.mac_and_cheese.add_ingredient(self.cheese, 2)
        self.mac_and_cheese.add_ingredient(self.mac, 8)

        self.assertIn(self.cheese, self.mac_and_cheese.ingredients)
        self.assertIn(self.mac, self.mac_and_cheese.ingredients)

    def test_you_can_get_total_calories(self):
        """You can get total number of calories in a recipe"""
        self.mac_and_cheese.add_ingredient(self.cheese, 2)
        self.mac_and_cheese.add_ingredient(self.mac, 8)

        self.assertEqual(self.mac_and_cheese.total_calories, 440)
