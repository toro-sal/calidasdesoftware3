"""
Unit tests for the ReservationManager class.
"""

import unittest
import os
from managers.reservation_manager import ReservationManager
from managers.reservation_manager import RESERVATION_DATA_FILE

TEST_RESERVATION_FILE = "test_reservations.json"


class TestReservationManager(unittest.TestCase):
    """Tests for ReservationManager functionalities."""

    def setUp(self):
        """Set up test environment before each test."""
        self._backup = None
        if os.path.exists(RESERVATION_DATA_FILE):
            with open(RESERVATION_DATA_FILE, 'r', encoding='utf-8') as f:
                self._backup = f.read()
            os.remove(RESERVATION_DATA_FILE)
        if os.path.exists(TEST_RESERVATION_FILE):
            os.remove(TEST_RESERVATION_FILE)
        self.manager = ReservationManager()

    def tearDown(self):
        """Clean up test environment after each test."""
        if os.path.exists(TEST_RESERVATION_FILE):
            os.remove(TEST_RESERVATION_FILE)
        if self._backup is not None:
            with open(RESERVATION_DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(self._backup)

    def test_create_reservation(self):
        """Test creating a new reservation."""
        res = self.manager.create_reservation({
            "reservation_id": "R100",
            "customer_id": "C200",
            "hotel_id": "H200",
            "room_number": 101,
            "check_in": "2025-01-01",
            "check_out": "2025-01-05"
        })
        self.assertEqual(res.reservation_id, "R100")
        self.assertEqual(res.customer_id, "C200")
        self.assertEqual(res.hotel_id, "H200")
        self.assertEqual(res.room_number, 101)
        self.assertEqual(res.check_in, "2025-01-01")
        self.assertEqual(res.check_out, "2025-01-05")

    def test_create_duplicate_reservation(self):
        """Test creating a duplicate reservation should raise ValueError."""
        self.manager.create_reservation({
            "reservation_id": "R101",
            "customer_id": "C201",
            "hotel_id": "H201",
            "room_number": 102,
            "check_in": "2025-01-10",
            "check_out": "2025-01-15"
        })
        with self.assertRaises(ValueError):
            self.manager.create_reservation({
                "reservation_id": "R101",  # Duplicate ID
                "customer_id": "C202",
                "hotel_id": "H202",
                "room_number": 103,
                "check_in": "2025-02-01",
                "check_out": "2025-02-05"
            })

    def test_cancel_reservation(self):
        """Test canceling a reservation."""
        self.manager.create_reservation({
            "reservation_id": "R102",
            "customer_id": "C202",
            "hotel_id": "H202",
            "room_number": 102,
            "check_in": "2025-03-01",
            "check_out": "2025-03-05"
        })
        # First cancellation should return True
        self.assertTrue(self.manager.cancel_reservation("R102"))
        # Second cancellation should return False, since it's already removed
        self.assertFalse(self.manager.cancel_reservation("R102"))

    def test_get_reservation_by_id_not_found(self):
        """Test searching for a non-existent reservation returns None."""
        res = self.manager.get_reservation_by_id("NonExistent")
        self.assertIsNone(res)

    def test_create_reservation_invalid_dates(self):
        """Test creating a reservation with "
        "invalid dates should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.create_reservation({
                "reservation_id": "R200",
                "customer_id": "C300",
                "hotel_id": "H300",
                "room_number": 105,
                "check_in": "2025-05-10",
                "check_out": "2025-05-01"
            })

    def test_cancel_nonexistent_reservation(self):
        """Test canceling a non-existent "
        "reservation should return False."""
        self.assertFalse(self.manager.cancel_reservation("FakeID"))

    def test_create_reservation_nonexistent_hotel(self):
        """Test creating a reservation for "
        "a non-existent hotel should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.create_reservation({
                "reservation_id": "R201",
                "customer_id": "C301",
                "hotel_id": "NonExistent",
                "room_number": 200,
                "check_in": "2025-06-01",
                "check_out": "2025-06-05"
            })

    def test_create_reservation_nonexistent_customer(self):
        """Test creating a reservation for a "
        "non-existent customer should raise ValueError."""
        with self.assertRaises(ValueError):
            self.manager.create_reservation({
                "reservation_id": "R202",
                "customer_id": "NonExistent",
                "hotel_id": "H302",
                "room_number": 205,
                "check_in": "2025-07-01",
                "check_out": "2025-07-05"
            })


if __name__ == '__main__':
    unittest.main()
