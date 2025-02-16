"""
Module defining the Reservation class, compliant with PEP8, Flake8, and Pylint.
"""

from dataclasses import dataclass
from datetime import date


@dataclass
class Reservation:
    """
    Represents a reservation with basic attributes.
    """
    reservation_id: str
    customer_id: str
    hotel_id: str
    room_number: int
    check_in: date
    check_out: date

    def __post_init__(self):
        """
        Validates the reservation details after initialization.
        """
        if self.check_in >= self.check_out:
            raise ValueError("Check-in date must be before check-out date.")

    def __str__(self):
        """
        Returns a string representation of the reservation.
        """
        return (f"Reservation({self.reservation_id}, "
                f"Customer={self.customer_id}, "
                f"Hotel={self.hotel_id}, Room={self.room_number}, "
                f"CheckIn={self.check_in}, CheckOut={self.check_out})")
