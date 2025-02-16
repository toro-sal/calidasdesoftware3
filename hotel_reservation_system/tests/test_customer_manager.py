"""
Unit tests for the ReservationManager class.
"""

import unittest
import os
from managers.customer_manager import CustomerManager, CUSTOMER_DATA_FILE

TEST_CUSTOMER_FILE = "test_customers.json"


class TestCustomerManager(unittest.TestCase):
    """Tests for CustomerManager functionalities."""

    def setUp(self):
        """Set up test environment before each test."""
        self._backup = None
        if os.path.exists(CUSTOMER_DATA_FILE):
            with open(CUSTOMER_DATA_FILE, 'r', encoding='utf-8') as f:
                self._backup = f.read()
            os.remove(CUSTOMER_DATA_FILE)
        if os.path.exists(TEST_CUSTOMER_FILE):
            os.remove(TEST_CUSTOMER_FILE)
        self.manager = CustomerManager()

    def tearDown(self):
        """Clean up test environment after each test."""
        if os.path.exists(TEST_CUSTOMER_FILE):
            os.remove(TEST_CUSTOMER_FILE)
        if self._backup is not None:
            with open(CUSTOMER_DATA_FILE, 'w', encoding='utf-8') as f:
                f.write(self._backup)

    def test_create_customer(self):
        """Test creating a new customer."""
        customer = self.manager.create_customer(
            "C100", "John Doe", "555-555-5555"
            )
        self.assertEqual(customer.customer_id, "C100")
        self.assertEqual(customer.name, "John Doe")
        self.assertEqual(customer.phone, "555-555-5555")

    def test_create_duplicate_customer(self):
        """Test creating a duplicate customer should raise ValueError."""
        self.manager.create_customer("C101", "Jane Doe", "555-555-0000")
        with self.assertRaises(ValueError):
            self.manager.create_customer(
                "C101", "Duplicate Name", "111-111-1111"
                )

    def test_delete_customer(self):
        """Test deleting a customer."""
        self.manager.create_customer("C102", "User Name", "999-999-9999")
        self.assertTrue(self.manager.delete_customer("C102"))
        self.assertFalse(self.manager.delete_customer("C102"))

    def test_modify_customer(self):
        """Test modifying customer information."""
        self.manager.create_customer("C103", "User Name", "999-999-9999")
        modified = self.manager.modify_customer_information(
            "C103", name="New Name", phone="888-888-8888"
            )
        self.assertTrue(modified)
        cust = self.manager.get_customer_by_id("C103")
        self.assertEqual(cust.name, "New Name")
        self.assertEqual(cust.phone, "888-888-8888")

    def test_get_customer_by_id_not_found(self):
        """Test searching for a non-existent customer returns None."""
        cust = self.manager.get_customer_by_id("NonExistent")
        self.assertIsNone(cust)


if __name__ == '__main__':
    unittest.main()
