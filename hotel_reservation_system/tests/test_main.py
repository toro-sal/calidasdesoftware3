"""Unit tests for main module in the hotel reservation system."""

import unittest
from unittest.mock import patch
import main


class TestMain(unittest.TestCase):
    """Tests for the main module initialization."""

    @patch('managers.hotel_manager.HotelManager')
    @patch('managers.customer_manager.CustomerManager')
    @patch('managers.reservation_manager.ReservationManager')
    def test_main_initialization(
        self,
        mock_reservation_manager,
        mock_customer_manager,
        mock_hotel_manager
    ):

        """Test that the main function initializes all managers correctly."""
        main.main()

        mock_hotel_manager.assert_called_once()
        mock_customer_manager.assert_called_once()
        mock_reservation_manager.assert_called_once()


if __name__ == '__main__':
    unittest.main()
