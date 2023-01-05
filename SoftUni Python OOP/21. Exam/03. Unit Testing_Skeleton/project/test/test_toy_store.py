from unittest import TestCase, main
from project.toy_store import ToyStore


class TestBookstore(TestCase):

    def setUp(self):
        self.store = ToyStore()

    def test_add_toy_shelf_Doesnt_Exists(self):
        with self.assertRaises(Exception) as ve:
            self.store.add_toy("Z", "ball")

        self.assertEqual("Shelf doesn't exist!", str(ve.exception))

    def test_add_toy_in_shelf_already(self):
        with self.assertRaises(Exception) as ve:
            self.store.add_toy("A", "ball")
            self.store.add_toy("A", "ball")

        self.assertEqual("Toy is already in shelf!", str(ve.exception))

    def test_add_toy_shelf_is_taken(self):
        with self.assertRaises(Exception) as ve:
            self.store.add_toy("A", "ball")
            self.store.add_toy("A", "batt")

        self.assertEqual("Shelf is already taken!", str(ve.exception))

    def test_add_toy_success(self):
        self.assertEqual(self.store.add_toy("A", "ball"),
                         "Toy:ball placed successfully!")

    def test_remove_toy_shelf_doesnt_exists(self):
        with self.assertRaises(Exception) as ve:
            self.store.remove_toy("Z", "ball")

        self.assertEqual("Shelf doesn't exist!", str(ve.exception))

    def test_toy_not_in_shelf(self):
        with self.assertRaises(Exception) as ve:
            self.store.remove_toy("A", "ball")

        self.assertEqual("Toy in that shelf doesn't exists!",
                         str(ve.exception))

    def test_remove_toy_success(self):
        self.store.add_toy("A", "ball")
        self.assertEqual(self.store.remove_toy("A", "ball"),
                         "Remove toy:ball successfully!")


    def test_constructor(self):
            self.assertDictEqual(self.store.toy_shelf, {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        })

    def test_randombba(self):
        self.assertEqual(self.store.toy_shelf["A"], "None")

if __name__ == '__main__':
    main()
