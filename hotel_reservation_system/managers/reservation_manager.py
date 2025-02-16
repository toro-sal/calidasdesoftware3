"""
Reservation Manager Module

This module provides a class to manage hotel reservations, including:
- Loading and saving reservations from a JSON file.
- Creating and canceling reservations.
- Retrieving reservation details.
"""

import json
import os
import logging
from typing import List, Optional
from models.reservation import Reservation

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
    )  # Ruta absoluta del script
RESERVATION_DATA_FILE = os.path.join(BASE_DIR, "../data/reservations.json")


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
                        reservation = Reservation(**item)
                        self.reservations.append(reservation)
                    except (KeyError, ValueError, TypeError) as error:
                        logging.warning("Error loading reservation "
                                        "record: %s => %s", item, error)
        except (json.JSONDecodeError, OSError) as error:
            logging.error("Error reading reservation file: %s", error)

    def save_reservations(self) -> None:
        """
        Saves reservation data to the JSON file.
        """
        data = [res.__dict__ for res in self.reservations]
        with open(RESERVATION_DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def create_reservation(self, reservation_data: dict) -> Reservation:
        """
        Creates a new Reservation if not already existing.
        """
        if (
            self.get_reservation_by_id(reservation_data["reservation_id"])
            is not None
        ):
            raise ValueError(
                f"Reservation with ID '{reservation_data['reservation_id']}'"
                " already exists."
            )

        new_reservation = Reservation(**reservation_data)
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

    def get_reservation_by_id(
        self, reservation_id: str
    ) -> Optional[Reservation]:

        """
        Returns a Reservation object by ID or None if not found.
        """
        return next(
            (
                res
                for res in self.reservations
                if res.reservation_id == reservation_id
            ),
            None
        )

    def display_reservation_information(self, reservation_id: str) -> None:
        """
        Prints the reservation information to the console.
        """
        reservation = self.get_reservation_by_id(reservation_id)
        if reservation:
            logging.info(
                "Reservation ID: %s\nCustomer ID: %s\nHotel ID:"
                " %s\nRoom Number: %d\nCheck-In: %s\nCheck-Out: %s",
                reservation.reservation_id,
                reservation.customer_id,
                reservation.hotel_id,
                reservation.room_number,
                reservation.check_in,
                reservation.check_out,
            )
        else:
            logging.warning("No reservation "
                            "found with ID '%s'.", reservation_id)
