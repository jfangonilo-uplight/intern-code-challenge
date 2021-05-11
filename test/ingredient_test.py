from unittest import TestCase


class IngredientTest(TestCase):
    def test_it_exists(self):
        """ Ingredient class can be instantiated with 3 parameters"""
        ingredient = Ingredient("Cheese", "oz", 50)

        self.assertIsInstance(ingredient, Ingredient)

    def test_it_has_attributes(self):
        """Ingredient class can return its name, unit of measurement, and calories per unit"""
        ingredient = Ingredient("Cheese", "oz", 50)

        self.assertEqual(ingredient.name, "Cheese")
        self.assertEqual(ingredient.unit, "oz")
        self.assertEqual(ingredient.calories, 50)
