"""
PEP8/Flake8/Pylint-compliant definition for the Hotel class.
"""

class Hotel:
    """
    Represents a Hotel with basic attributes.
    """
    def __init__(self, hotel_id: str, name: str, location: str, total_rooms: int):
        """
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
        String representation of the hotel.
        """
        return f"Hotel({self.hotel_id}, {self.name}, {self.location}, rooms={self.total_rooms})"
