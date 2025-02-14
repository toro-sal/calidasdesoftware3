"""
Hotel class.
"""


class Hotel:
    """
    Represents a Hotel with basic attributes.
    """

    def __init__(
            self, hotel_id: str, name: str, location: str, total_rooms: int
            ):
        """
        Initializes a new Hotel instance.

        :param hotel_id: Unique identifier for the hotel
        :param name: Hotel name
        :param location: Hotel location
        :param total_rooms: Number of rooms in the hotel
        """
        self.hotel_id = hotel_id
        self.name = name
        self.location = location
        self.total_rooms = total_rooms

    def __str__(self):
        """
        Returns the string representation of the hotel.
        """
        return (
            f"Hotel({self.hotel_id}, {self.name}, {self.location}, "
            f"rooms={self.total_rooms})"
        )

    def to_dict(self):
        """
        Returns a dictionary representation of the hotel.
        """
        return {
            "hotel_id": self.hotel_id,
            "name": self.name,
            "location": self.location,
            "total_rooms": self.total_rooms,
        }
