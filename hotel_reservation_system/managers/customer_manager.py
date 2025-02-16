"""
Manager class that handles CRUD operations for Customer objects.
Stores data in a JSON file.
"""

import json
import os
from typing import List, Optional
from models.customer import Customer

BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
    )

CUSTOMER_DATA_FILE = os.path.join(
    BASE_DIR, "../data/customers.json"
    )


class CustomerManager:
    """
    Manages Customer objects, including creation, deletion, display,
    modification, and saving/loading to/from JSON.
    """

    def __init__(self):
        self.customers: List[Customer] = []
        self.load_customers()

    def load_customers(self) -> None:
        """
        Loads customer data from JSON file.
        Invalid records are logged and skipped.
        """
        self.customers = []
        if not os.path.exists(CUSTOMER_DATA_FILE):
            return

        try:
            with open(CUSTOMER_DATA_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                for item in data:
                    try:
                        customer = Customer(
                            customer_id=item["customer_id"],
                            name=item["name"],
                            phone=item["phone"]
                        )
                        self.customers.append(customer)
                    except (KeyError, ValueError, TypeError) as error:
                        print("Error loading "
                              f"customer record: {item} => {error}")
        except (json.JSONDecodeError, OSError) as error:
            print(f"Error reading customer file: {error}")

    def save_customers(self) -> None:
        """
        Saves customer data to JSON file.
        """
        data = []
        for customer in self.customers:
            data.append({
                "customer_id": customer.customer_id,
                "name": customer.name,
                "phone": customer.phone
            })
        with open(CUSTOMER_DATA_FILE, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def create_customer(
            self, customer_id: str, name: str, phone: str
            ) -> Customer:
        """
        Creates a new Customer and saves it.
        """
        if self.get_customer_by_id(customer_id) is not None:
            raise ValueError("Customer with "
                             f"ID '{customer_id}' already exists.")

        new_customer = Customer(customer_id, name, phone)
        self.customers.append(new_customer)
        self.save_customers()
        return new_customer

    def delete_customer(self, customer_id: str) -> bool:
        """
        Deletes a Customer by its ID if it exists.
        """
        customer = self.get_customer_by_id(customer_id)
        if customer:
            self.customers.remove(customer)
            self.save_customers()
            return True
        return False

    def display_customer_information(self, customer_id: str) -> None:
        """
        Prints customer information to console.
        """
        customer = self.get_customer_by_id(customer_id)
        if customer:
            print(f"Customer ID: {customer.customer_id}")
            print(f"Name: {customer.name}")
            print(f"Phone: {customer.phone}")
        else:
            print(f"No customer found with ID '{customer_id}'.")

    def modify_customer_information(self, customer_id: str, **kwargs) -> bool:
        """
        Modifies customer information (name, phone).
        """
        customer = self.get_customer_by_id(customer_id)
        if not customer:
            return False

        if "name" in kwargs:
            customer.name = kwargs["name"]
        if "phone" in kwargs:
            customer.phone = kwargs["phone"]
        self.save_customers()
        return True

    def get_customer_by_id(self, customer_id: str) -> Optional[Customer]:
        """
        Returns a Customer object by ID or None.
        """
        for customer in self.customers:
            if customer.customer_id == customer_id:
                return customer
        return None
