from unittest import TestCase


class CookBookTest(TestCase):
    def setUp(self):
        self.cook_book = CookBook()

        self.cheese = Ingredient("Cheese", "C", 100)
        self.mac = Ingredient("Macaroni", "oz", 30)
        self.mac_and_cheese = Recipe("Mac and Cheese")
        self.mac_and_cheese.add_ingredient(self.mac, 8)
        self.mac_and_cheese.add_ingredient(self.cheese, 2)

        self.ground_beef = Ingredient("Ground Beef", "oz", 100)
        self.bun = Ingredient("Bun", "g", 1)
        self.burger = Recipe("Burger")
        self.burger.add_ingredient(self.ground_beef, 4)
        self.burger.add_ingredient(self.bun, 100)

    def test_you_can_add_recipes(self):
        """Recipes start empty until added"""
        self.assertEqual(self.cook_book.recipes, [])

        self.cook_book.add_recipe(self.mac_and_cheese)
        self.cook_book.add_recipe(self.burger)

        self.assertIn(self.mac_and_cheese, self.cook_book.recipes)
        self.assertIn(self.burger, self.cook_book.recipes)

    def test_summary(self):
        """If you've made it this far, congrats

        Hint: You may add additional specs to other classes to help build this
        """
        self.cook_book.add_recipe(self.mac_and_cheese)
        self.cook_book.add_recipe(self.burger)

        expected = [
            {
                "name": "Mac and Cheese",
                "details": {
                    "ingredients": [
                        {
                            "ingredient": "Macaroni",
                            "amount": "8 oz"
                        },
                        {
                            "ingredient": "Cheese",
                            "amount": "2 C"
                        }
                    ]
                },
                "total_calories": 440
            },
            {
                "name": "Burger",
                "details": {
                    "ingredients": [
                        {
                            "ingredient": "Ground Beef",
                            "amount": "4 oz"
                        },
                        {
                            "ingredient": "Bun",
                            "amount": "100 g"
                        }
                    ]
                },
                "total_calories": 500
            }
        ]
        self.assertEqual(self.cook_book.summary, expected)
