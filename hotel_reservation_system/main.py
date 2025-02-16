"""
Menu-driven console application for the Hotel Reservation System.
"""
import sys
from managers.hotel_manager import HotelManager
from managers.customer_manager import CustomerManager
from managers.reservation_manager import ReservationManager


def main():
    """Main function for the Hotel Reservation System."""
    hotel_manager = HotelManager()
    customer_manager = CustomerManager()
    reservation_manager = ReservationManager()
    menu_options = {
        "1": create_hotel,
        "2": delete_hotel,
        "3": display_hotel,
        "4": modify_hotel,
        "5": create_reservation,
        "6": cancel_reservation,
        "7": create_customer,
        "8": delete_customer,
        "9": display_customer,
        "10": modify_customer,
        "11": display_reservation,
        "12": exit_system
    }

    while True:
        print("\n===== HOTEL RESERVATION SYSTEM =====")
        print("1.  Create Hotel")
        print("2.  Delete Hotel")
        print("3.  Display Hotel Information")
        print("4.  Modify Hotel Information")
        print("5.  Reserve a Room (Create a Reservation)")
        print("6.  Cancel a Reservation")
        print("7.  Create Customer")
        print("8.  Delete Customer")
        print("9.  Display Customer Information")
        print("10. Modify Customer Information")
        print("11. Display Reservation Information")
        print("12. Exit")
        choice = input("\nEnter your choice (1-12): ")

        action = menu_options.get(choice, invalid_choice)
        action(hotel_manager, customer_manager, reservation_manager)


def create_hotel(hotel_manager, *_):
    """Handles hotel creation."""
    hotel_id = input("Enter Hotel ID: ")
    name = input("Enter Hotel Name: ")
    location = input("Enter Location: ")
    try:
        total_rooms = int(input("Enter total number of rooms: "))
        new_hotel = hotel_manager.create_hotel(
            hotel_id, name, location, total_rooms
            )
        print(f"Successfully created hotel: {new_hotel}")
    except ValueError:
        print("Invalid input. Operation cancelled.")


def delete_hotel(hotel_manager, *_):
    """Handles hotel deletion."""
    hotel_id = input("Enter Hotel ID to delete: ")
    if hotel_manager.delete_hotel(hotel_id):
        print(f"Hotel '{hotel_id}' was deleted.")
    else:
        print(f"No hotel found with ID '{hotel_id}'.")


def display_hotel(hotel_manager, *_):
    """Displays hotel information."""
    hotel_id = input("Enter Hotel ID to display: ")
    hotel_manager.display_hotel_information(hotel_id)


def modify_hotel(hotel_manager, *_):
    """Modifies hotel information."""
    hotel_id = input("Enter Hotel ID to modify: ")
    name = input("Enter new Hotel Name (press Enter to skip): ")
    location = input("Enter new Location (press Enter to skip): ")
    rooms_str = input("Enter new total rooms (press Enter to skip): ")
    kwargs = {"name": name, "location": location} if name or location else {}
    if rooms_str:
        try:
            kwargs["total_rooms"] = int(rooms_str)
        except ValueError:
            print("Invalid input for total rooms. Skipped.")
    if kwargs and hotel_manager.modify_hotel_information(hotel_id, **kwargs):
        print(f"Hotel '{hotel_id}' updated successfully.")
    else:
        print("No changes made or no hotel found.")


def create_reservation(_, reservation_manager):
    """Handles reservation creation."""
    reservation_id = input("Enter Reservation ID: ")
    customer_id = input("Enter Customer ID: ")
    hotel_id = input("Enter Hotel ID: ")
    try:
        room_number = int(input("Enter room number: "))
        check_in = input("Enter Check-In date (YYYY-MM-DD): ")
        check_out = input("Enter Check-Out date (YYYY-MM-DD): ")
        new_res = reservation_manager.create_reservation(
            reservation_id,
            customer_id,
            hotel_id,
            room_number,
            check_in,
            check_out
        )
        print(f"Reservation created successfully: {new_res}")
    except ValueError:
        print("Invalid input. Operation cancelled.")


def cancel_reservation(reservation_manager):
    """Handles reservation cancellation."""
    reservation_id = input("Enter Reservation ID to cancel: ")
    if reservation_manager.cancel_reservation(reservation_id):
        print(f"Reservation '{reservation_id}' was cancelled.")
    else:
        print(f"No reservation found with ID '{reservation_id}'.")


def create_customer(_, customer_manager, __):
    """Handles customer creation."""
    customer_id = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    phone = input("Enter Customer Phone: ")
    try:
        new_cust = customer_manager.create_customer(customer_id, name, phone)
        print(f"Customer created successfully: {new_cust}")
    except ValueError:
        print("Error creating customer.")


def delete_customer(_, customer_manager, __):
    """Handles customer deletion."""
    customer_id = input("Enter Customer ID to delete: ")
    if customer_manager.delete_customer(customer_id):
        print(f"Customer '{customer_id}' was deleted.")
    else:
        print(f"No customer found with ID '{customer_id}'.")


def display_customer(_, customer_manager, __):
    """Displays customer information."""
    customer_id = input("Enter Customer ID to display: ")
    customer_manager.display_customer_information(customer_id)


def modify_customer(_, customer_manager, __):
    """Modifies customer information."""
    customer_id = input("Enter Customer ID to modify: ")
    name = input("Enter new Name (press Enter to skip): ")
    phone = input("Enter new Phone (press Enter to skip): ")
    kwargs = {"name": name, "phone": phone} if name or phone else {}
    if (kwargs and
            customer_manager.modify_customer_information(
                customer_id, **kwargs)):
        print(f"Customer '{customer_id}' updated successfully.")
    else:
        print("No changes made or no customer found.")


def display_reservation(reservation_manager):
    """Displays reservation information."""
    reservation_id = input("Enter Reservation ID to display: ")
    reservation_manager.display_reservation_information(reservation_id)


def exit_system(*_):
    """Exits the application."""
    print("Exiting the Hotel Reservation System.")
    sys.exit()


def invalid_choice(*_):
    """Handles invalid menu choices."""
    print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
