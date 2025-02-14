"""
Customer class.
"""


class Customer:
    """
    Represents a Customer with basic attributes.
    """

    def __init__(self, customer_id: str, name: str, phone: str):
        """
        Initializes a new Customer instance.

        :param customer_id: Unique identifier for the customer
        :param name: Customer name
        :param phone: Customer phone number
        """
        self.customer_id = customer_id
        self.name = name
        self.phone = phone

    def __str__(self):
        """
        Returns the string representation of the customer.
        """
        return f"Customer({self.customer_id}, {self.name}, {self.phone})"

    def to_dict(self):
        """
        Returns a dictionary representation of the customer.
        """
        return {
            "customer_id": self.customer_id,
            "name": self.name,
            "phone": self.phone,
        }
