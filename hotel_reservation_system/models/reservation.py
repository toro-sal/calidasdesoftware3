"""
PEP8/Flake8/Pylint-compliant definition for the Reservation class.
"""

class Reservation:
    """
    Represents a Reservation with basic attributes.
    """
    def __init__(self,
                 reservation_id: str,
                 customer_id: str,
                 hotel_id: str,
                 room_number: int,
                 check_in: str,
                 check_out: str):
        """
        :param reservation_id: Unique identifier for the reservation
        :param customer_id: Unique identifier of the customer
        :param hotel_id: Unique identifier of the hotel
        :param room_number: Assigned room number in the hotel
        :param check_in: Check-in date (string or datetime)
        :param check_out: Check-out date (string or datetime)
        """
        self.reservation_id = reservation_id
        self.customer_id = customer_id
        self.hotel_id = hotel_id
        self.room_number = room_number
        self.check_in = check_in
        self.check_out = check_out

    def __str__(self):
        """
        String representation of the reservation.
        """
        return (f"Reservation({self.reservation_id}, Customer={self.customer_id}, "
                f"Hotel={self.hotel_id}, Room={self.room_number}, "
                f"CheckIn={self.check_in}, CheckOut={self.check_out})")
