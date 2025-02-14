"""
Reservation class.
"""


from dataclasses import dataclass


@dataclass
class ReservationDetails:
    """
    Holds the details of a reservation.
    """
    reservation_id: str
    customer_id: str
    hotel_id: str
    room_number: int
    check_in: str
    check_out: str


class Reservation:
    """
    Represents a Reservation with basic attributes.
    """

    def __init__(self, details: ReservationDetails):
        """
        Initializes a new Reservation instance.

        :param details: ReservationDetails
         object containing all reservation data.
        """
        self.details = details

    def __str__(self):
        """
        Returns the string representation of the reservation.
        """
        return (
            f"Reservation({self.details.reservation_id}, "
            f"Customer={self.details.customer_id}, "
            f"Hotel={self.details.hotel_id}, "
            f"Room={self.details.room_number}, "
            f"CheckIn={self.details.check_in}, "
            f"CheckOut={self.details.check_out})"
        )

    def to_dict(self):
        """
        Returns a dictionary representation of the reservation.
        """
        return {
            "reservation_id": self.details.reservation_id,
            "customer_id": self.details.customer_id,
            "hotel_id": self.details.hotel_id,
            "room_number": self.details.room_number,
            "check_in": self.details.check_in,
            "check_out": self.details.check_out,
        }
