"""
Manager class that handles CRUD operations for Hotel objects.
Stores data in a JSON file.
"""

import json
import os
from typing import List, Optional

from models.hotel import Hotel

HOTEL_DATA_FILE = os.path.join(
    "hotel_reservation_system", "data", "hotels.json"
    )


class HotelManager:
    """
    Manages Hotel objects, including creation, deletion, display,
    modification, and saving/loading to/from JSON.
    """

    def __init__(self):
        self.hotels: List[Hotel] = []
        self.load_hotels()

    def load_hotels(self) -> None:
        """
        Loads hotel data from the JSON file.
        Invalid records are logged to console and skipped.
        """
        self.hotels = []
        if not os.path.exists(HOTEL_DATA_FILE):
            return

        try:
            with open(HOTEL_DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    try:
                        hotel = Hotel(
                            hotel_id=item["hotel_id"],
                            name=item["name"],
                            location=item["location"],
                            total_rooms=int(item["total_rooms"])
                        )
                        self.hotels.append(hotel)
                    except (KeyError, ValueError, TypeError) as error:
                        print(f"Error loading hotel record: {item} => {error}")
        except (json.JSONDecodeError, OSError) as error:
            print(f"Error reading hotel file: {error}")

    def save_hotels(self) -> None:
        """
        Saves hotel data to the JSON file.
        """
        data = []
        for hotel in self.hotels:
            data.append({
                "hotel_id": hotel.hotel_id,
                "name": hotel.name,
                "location": hotel.location,
                "total_rooms": hotel.total_rooms
            })
        with open(HOTEL_DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def create_hotel(
            self, hotel_id: str, name: str, location: str, total_rooms: int
            ) -> Hotel:
        """
        Creates a new Hotel and saves it to file.
        """
        # Check if hotel ID already exists
        if self.get_hotel_by_id(hotel_id) is not None:
            raise ValueError(f"Hotel with ID '{hotel_id}' already exists.")

        new_hotel = Hotel(hotel_id, name, location, total_rooms)
        self.hotels.append(new_hotel)
        self.save_hotels()
        return new_hotel

    def delete_hotel(self, hotel_id: str) -> bool:
        """
        Deletes a Hotel by its ID if it exists.
        """
        hotel = self.get_hotel_by_id(hotel_id)
        if hotel:
            self.hotels.remove(hotel)
            self.save_hotels()
            return True
        return False

    def display_hotel_information(self, hotel_id: str) -> None:
        """
        Prints hotel information to console.
        """
        hotel = self.get_hotel_by_id(hotel_id)
        if hotel:
            print(f"Hotel ID: {hotel.hotel_id}")
            print(f"Name: {hotel.name}")
            print(f"Location: {hotel.location}")
            print(f"Total Rooms: {hotel.total_rooms}")
        else:
            print(f"No hotel found with ID '{hotel_id}'.")

    def modify_hotel_information(self, hotel_id: str, **kwargs) -> bool:
        """
        Modifies hotel information (name, location, total_rooms).
        """
        hotel = self.get_hotel_by_id(hotel_id)
        if not hotel:
            return False

        if "name" in kwargs:
            hotel.name = kwargs["name"]
        if "location" in kwargs:
            hotel.location = kwargs["location"]
        if "total_rooms" in kwargs:
            hotel.total_rooms = int(kwargs["total_rooms"])
        self.save_hotels()
        return True

    def get_hotel_by_id(self, hotel_id: str) -> Optional[Hotel]:
        """
        Returns a Hotel object by ID, or None if not found.
        """
        for hotel in self.hotels:
            if hotel.hotel_id == hotel_id:
                return hotel
        return None
