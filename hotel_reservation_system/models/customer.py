"""
PEP8/Flake8/Pylint-compliant definition for the Customer class.
"""

class Customer:
    """
    Represents a Customer with basic attributes.
    """
    def __init__(self, customer_id: str, name: str, phone: str):
        """
        :param customer_id: Unique identifier for the customer
        :param name: Customer name
        :param phone: Customer phone number
        """
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def __str__(self):
        """
        String representation of the customer.
        """
        return f"Customer({self.customer_id}, {self.name}, {self.phone})"
