"""
Console application demonstrating the Hotel Reservation System usage.
"""

from managers.hotel_manager import HotelManager
from managers.customer_manager import CustomerManager
from managers.reservation_manager import ReservationManager


def main():
    """
    Initializes and demonstrates the usage of the hotel reservation system.
    """
    hotel_manager = HotelManager()
    customer_manager = CustomerManager()
    reservation_manager = ReservationManager()
    # Example usage to avoid unused variable warnings
    print(f"Hotel Manager initialized: {hotel_manager}")
    print(f"Customer Manager initialized: {customer_manager}")
    print(f"Reservation Manager initialized: {reservation_manager}")


if __name__ == "__main__":
    main()
