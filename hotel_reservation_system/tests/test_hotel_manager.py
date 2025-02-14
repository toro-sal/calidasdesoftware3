import unittest
import os
import json
from managers.hotel_manager import HotelManager, HOTEL_DATA_FILE

TEST_HOTEL_FILE = "test_hotels.json"

class TestHotelManager(unittest.TestCase):
    def setUp(self):
        # Backup original file if exists
        self._backup = None
        if os.path.exists(HOTEL_DATA_FILE):
            with open(HOTEL_DATA_FILE, 'r', encoding='utf-8') as f:
                self._backup = f.read()
            os.remove(HOTEL_DATA_FILE)
        # Point to test file
        if os.path.exists(TEST_HOTEL_FILE):
            os.remove(TEST_HOTEL_FILE)
        self.manager = HotelManager()

    def tearDown(self):
        # Remove test file
        if os.path.exists(TEST_HOTEL_FILE):
            os.remove(TEST_HOTEL_FILE)
        # Restore original file
        if self._backup is not None:
            with open(HOTEL_DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(self._backup)

    def test_create_hotel(self):
        new_hotel = self.manager.create_hotel("H100", "Test Hotel", "Test City", 100)
        self.assertEqual(new_hotel.hotel_id, "H100")
        self.assertEqual(new_hotel.name, "Test Hotel")
        self.assertEqual(new_hotel.location, "Test City")
        self.assertEqual(new_hotel.total_rooms, 100)

    def test_create_duplicate_hotel(self):
        self.manager.create_hotel("H101", "Test Hotel", "Test City", 100)
        with self.assertRaises(ValueError):
            self.manager.create_hotel("H101", "Test2", "Test City2", 150)

    def test_delete_hotel(self):
        self.manager.create_hotel("H102", "Test Hotel", "Test City", 100)
        self.assertTrue(self.manager.delete_hotel("H102"))
        self.assertFalse(self.manager.delete_hotel("H102"))

    def test_modify_hotel_information(self):
        self.manager.create_hotel("H103", "Test Hotel", "Test City", 100)
        modified = self.manager.modify_hotel_information("H103", name="New Name", total_rooms=200)
        self.assertTrue(modified)
        hotel = self.manager.get_hotel_by_id("H103")
        self.assertEqual(hotel.name, "New Name")
        self.assertEqual(hotel.total_rooms, 200)

    def test_get_hotel_by_id_not_found(self):
        hotel = self.manager.get_hotel_by_id("NonExistent")
        self.assertIsNone(hotel)

if __name__ == '__main__':
    unittest.main()
