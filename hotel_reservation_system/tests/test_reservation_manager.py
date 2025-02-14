import unittest
import os
import json
from managers.reservation_manager import ReservationManager, RESERVATION_DATA_FILE

TEST_RESERVATION_FILE = "test_reservations.json"

class TestReservationManager(unittest.TestCase):
    def setUp(self):
        # Backup original file if exists
        self._backup = None
        if os.path.exists(RESERVATION_DATA_FILE):
            with open(RESERVATION_DATA_FILE, 'r', encoding='utf-8') as f:
                self._backup = f.read()
            os.remove(RESERVATION_DATA_FILE)
        # Initialize manager
        if os.path.exists(TEST_RESERVATION_FILE):
            os.remove(TEST_RESERVATION_FILE)
        self.manager = ReservationManager()

    def tearDown(self):
        # Remove test file
        if os.path.exists(TEST_RESERVATION_FILE):
            os.remove(TEST_RESERVATION_FILE)
        # Restore original file
        if self._backup is not None:
            with open(RESERVATION_DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(self._backup)

    def test_create_reservation(self):
        res = self.manager.create_reservation("R100", "C200", "H200", 101, "2025-01-01", "2025-01-05")
        self.assertEqual(res.reservation_id, "R100")
        self.assertEqual(res.customer_id, "C200")
        self.assertEqual(res.hotel_id, "H200")
        self.assertEqual(res.room_number, 101)
        self.assertEqual(res.check_in, "2025-01-01")
        self.assertEqual(res.check_out, "2025-01-05")

    def test_create_duplicate_reservation(self):
        self.manager.create_reservation("R101", "C201", "H201", 102, "2025-01-10", "2025-01-15")
        with self.assertRaises(ValueError):
            self.manager.create_reservation("R101", "C202", "H202", 103, "2025-02-01", "2025-02-05")

    def test_cancel_reservation(self):
        self.manager.create_reservation("R102", "C202", "H202", 102, "2025-03-01", "2025-03-05")
        self.assertTrue(self.manager.cancel_reservation("R102"))
        self.assertFalse(self.manager.cancel_reservation("R102"))

    def test_get_reservation_by_id_not_found(self):
        res = self.manager.get_reservation_by_id("NonExistent")
        self.assertIsNone(res)

if __name__ == '__main__':
    unittest.main()
