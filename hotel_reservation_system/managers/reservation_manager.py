"""
Manager class that handles operations for Reservations.
Stores data in a JSON file.
"""

import json
import os
from typing import List, Optional

from models.reservation import Reservation

RESERVATION_DATA_FILE = os.path.join("hotel_reservation_system","data", "reservations.json")


class ReservationManager:
    """
    Manages Reservation objects, including creation, cancellation,
    and saving/loading to/from JSON.
    """

    def __init__(self):
        self.reservations: List[Reservation] = []
        self.load_reservations()

    def load_reservations(self) -> None:
        """
        Loads reservation data from the JSON file.
        Invalid records are logged to console and skipped.
        """
        self.reservations = []
        if not os.path.exists(RESERVATION_DATA_FILE):
            return

        try:
            with open(RESERVATION_DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    try:
                        reservation = Reservation(
                            reservation_id=item["reservation_id"],
                            customer_id=item["customer_id"],
                            hotel_id=item["hotel_id"],
                            room_number=int(item["room_number"]),
                            check_in=item["check_in"],
                            check_out=item["check_out"]
                        )
                        self.reservations.append(reservation)
                    except (KeyError, ValueError, TypeError) as error:
                        print(f"Error loading reservation record: {item} => {error}")
        except (json.JSONDecodeError, OSError) as error:
            print(f"Error reading reservation file: {error}")

    def save_reservations(self) -> None:
        """
        Saves reservation data to the JSON file.
        """
        data = []
        for res in self.reservations:
            data.append({
                "reservation_id": res.reservation_id,
                "customer_id": res.customer_id,
                "hotel_id": res.hotel_id,
                "room_number": res.room_number,
                "check_in": res.check_in,
                "check_out": res.check_out
            })
        with open(RESERVATION_DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def create_reservation(self,
                           reservation_id: str,
                           customer_id: str,
                           hotel_id: str,
                           room_number: int,
                           check_in: str,
                           check_out: str) -> Reservation:
        """
        Creates a new Reservation if not already existing.
        """
        if self.get_reservation_by_id(reservation_id) is not None:
            raise ValueError(f"Reservation with ID '{reservation_id}' already exists.")

        new_reservation = Reservation(
            reservation_id,
            customer_id,
            hotel_id,
            room_number,
            check_in,
            check_out
        )
        self.reservations.append(new_reservation)
        self.save_reservations()
        return new_reservation

    def cancel_reservation(self, reservation_id: str) -> bool:
        """
        Cancels (deletes) a reservation by ID, if it exists.
        """
        reservation = self.get_reservation_by_id(reservation_id)
        if reservation:
            self.reservations.remove(reservation)
            self.save_reservations()
            return True
        return False

    def get_reservation_by_id(self, reservation_id: str) -> Optional[Reservation]:
        """
        Returns a Reservation object by ID or None if not found.
        """
        for res in self.reservations:
            if res.reservation_id == reservation_id:
                return res
        return None

    def display_reservation_information(self, reservation_id: str) -> None:
        """
        Prints the reservation information to the console.
        """
        reservation = self.get_reservation_by_id(reservation_id)
        if reservation:
            print(f"Reservation ID: {reservation.reservation_id}")
            print(f"Customer ID: {reservation.customer_id}")
            print(f"Hotel ID: {reservation.hotel_id}")
            print(f"Room Number: {reservation.room_number}")
            print(f"Check-In: {reservation.check_in}")
            print(f"Check-Out: {reservation.check_out}")
        else:
            print(f"No reservation found with ID '{reservation_id}'.")
