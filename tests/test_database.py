import src.database.database as db
import unittest


class test_Ingredients(unittest.TestCase):

    # TODO make add, rm, u methods testable

    def test_query_by_ingredient(self):
        self.assertDictEqual(
            dict(db.Ingredients.by_name('test')),
            {'id':0, 'unit':'kg', 'price_per_unit':5.0}
        )

    def test_query_by_id(self):
        self.assertDictEqual(
            dict(db.Ingredients.by_id(0)),
            {'ingredient':'test', 'unit':'kg', 'price_per_unit':5.0}
        )

    def test_query_id(self):
        self.assertEqual(
            db.Ingredients.q('test'),
            0
        )

class test_Foods(unittest.TestCase):

    def test_query_id(self):
        self.assertEqual(
            db.Foods.q('test'),
            0
        )

    def test_query_by_food(self):
        self.assertDictEqual(
            dict(db.Foods.by_name('test')),
            {'id':0, 'servings':3}
        )

    def test_query_by_id(self):
        self.assertDictEqual(
            dict(db.Foods.by_id(0)),
            {'food':'test', 'servings':3}
        )
        

    def test_query_ingredients(self):
        self.assertListEqual(
            [dict(row) for row in db.Foods.query_ingredients('test')],
            [
                {'ingredient_id': -2, 'ammount': 0.5, 'price_per_ammount': 5.0},
                {'ingredient_id': -1, 'ammount': 0.5, 'price_per_ammount': 1.0},
                {'ingredient_id': 0, 'ammount': 0.5, 'price_per_ammount': 2.5}
            ]
        )