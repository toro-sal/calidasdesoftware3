"""
Menu-driven console application for the Hotel Reservation System.
"""

from managers.hotel_manager import HotelManager
from managers.customer_manager import CustomerManager
from managers.reservation_manager import ReservationManager


def main():
    hotel_manager = HotelManager()
    customer_manager = CustomerManager()
    reservation_manager = ReservationManager()

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

        if choice == "1":
            # Create Hotel
            hotel_id = input("Enter Hotel ID: ")
            name = input("Enter Hotel Name: ")
            location = input("Enter Location: ")
            try:
                total_rooms = int(input("Enter total number of rooms: "))
            except ValueError:
                print("Invalid input for total rooms. Operation cancelled.")
                continue

            try:
                new_hotel = hotel_manager.create_hotel(
                    hotel_id, name, location, total_rooms
                )
                print(f"Successfully created hotel: {new_hotel}")
            except ValueError as err:
                print(f"Error creating hotel: {err}")

        elif choice == "2":
            # Delete Hotel
            hotel_id = input("Enter Hotel ID to delete: ")
            deleted = hotel_manager.delete_hotel(hotel_id)
            if deleted:
                print(f"Hotel '{hotel_id}' was deleted.")
            else:
                print(f"No hotel found with ID '{hotel_id}'.")

        elif choice == "3":
            # Display Hotel Information
            hotel_id = input("Enter Hotel ID to display: ")
            hotel_manager.display_hotel_information(hotel_id)

        elif choice == "4":
            # Modify Hotel Information
            hotel_id = input("Enter Hotel ID to modify: ")
            name = input("Enter new Hotel Name (press Enter to skip): ")
            location = input("Enter new Location (press Enter to skip): ")
            rooms_str = input("Enter new total rooms (press Enter to skip): ")

            kwargs = {}
            if name:
                kwargs["name"] = name
            if location:
                kwargs["location"] = location
            if rooms_str:
                try:
                    kwargs["total_rooms"] = int(rooms_str)
                except ValueError:
                    print("Invalid input for total rooms. Skipped changing room count.")

            if kwargs:
                modified = hotel_manager.modify_hotel_information(hotel_id, **kwargs)
                if modified:
                    print(f"Hotel '{hotel_id}' updated successfully.")
                else:
                    print(f"No hotel found with ID '{hotel_id}'.")
            else:
                print("No changes made.")

        elif choice == "5":
            # Reserve a Room (Create a Reservation)
            reservation_id = input("Enter a new Reservation ID: ")
            customer_id = input("Enter Customer ID for this reservation: ")
            hotel_id = input("Enter Hotel ID for this reservation: ")

            try:
                room_number = int(input("Enter room number to reserve: "))
            except ValueError:
                print("Invalid input for room number. Operation cancelled.")
                continue

            check_in = input("Enter Check-In date (e.g., 2025-03-01): ")
            check_out = input("Enter Check-Out date (e.g., 2025-03-05): ")

            try:
                new_res = reservation_manager.create_reservation(
                    reservation_id=reservation_id,
                    customer_id=customer_id,
                    hotel_id=hotel_id,
                    room_number=room_number,
                    check_in=check_in,
                    check_out=check_out
                )
                print(f"Reservation created successfully: {new_res}")
            except ValueError as err:
                print(f"Error creating reservation: {err}")

        elif choice == "6":
            # Cancel a Reservation
            reservation_id = input("Enter Reservation ID to cancel: ")
            cancelled = reservation_manager.cancel_reservation(reservation_id)
            if cancelled:
                print(f"Reservation '{reservation_id}' was cancelled.")
            else:
                print(f"No reservation found with ID '{reservation_id}'.")

        elif choice == "7":
            # Create Customer
            customer_id = input("Enter Customer ID: ")
            name = input("Enter Customer Name: ")
            phone = input("Enter Customer Phone: ")

            try:
                new_cust = customer_manager.create_customer(customer_id, name, phone)
                print(f"Customer created successfully: {new_cust}")
            except ValueError as err:
                print(f"Error creating customer: {err}")

        elif choice == "8":
            # Delete Customer
            customer_id = input("Enter Customer ID to delete: ")
            deleted = customer_manager.delete_customer(customer_id)
            if deleted:
                print(f"Customer '{customer_id}' was deleted.")
            else:
                print(f"No customer found with ID '{customer_id}'.")

        elif choice == "9":
            # Display Customer Information
            customer_id = input("Enter Customer ID to display: ")
            customer_manager.display_customer_information(customer_id)

        elif choice == "10":
            # Modify Customer Information
            customer_id = input("Enter Customer ID to modify: ")
            new_name = input("Enter new Name (press Enter to skip): ")
            new_phone = input("Enter new Phone (press Enter to skip): ")

            kwargs = {}
            if new_name:
                kwargs["name"] = new_name
            if new_phone:
                kwargs["phone"] = new_phone

            if kwargs:
                modified = customer_manager.modify_customer_information(
                    customer_id, **kwargs
                )
                if modified:
                    print(f"Customer '{customer_id}' updated successfully.")
                else:
                    print(f"No customer found with ID '{customer_id}'.")
            else:
                print("No changes made.")

        elif choice == "11":
            # Display Reservation Information
            reservation_id = input("Enter Reservation ID to display: ")
            reservation_manager.display_reservation_information(reservation_id)

        elif choice == "12":
            # Exit
            print("Exiting the Hotel Reservation System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
