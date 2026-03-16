import unittest
from src.loyalty_engine import classify_loyalty, customer_activity_status


class TestLoyaltyEngine(unittest.TestCase):

    def test_platinum_customer_classification(self):
        self.assertEqual(classify_loyalty(12000), "PLATINUM")

    def test_gold_customer_classification(self):
        self.assertEqual(classify_loyalty(7000), "GOLD")

    def test_silver_customer_classification(self):
        self.assertEqual(classify_loyalty(2000), "SILVER")

    def test_bronze_customer_classification(self):
        self.assertEqual(classify_loyalty(500), "BRONZE")

    def test_active_customer_with_orders(self):

        customer = {"status": "ACTIVE"}

        result = customer_activity_status(customer, 3)

        self.assertEqual(result, "ACTIVE_CUSTOMER")

    def test_active_customer_without_orders(self):

        customer = {"status": "ACTIVE"}

        result = customer_activity_status(customer, 0)

        self.assertEqual(result, "INACTIVE_CUSTOMER")

    def test_inactive_customer_status(self):

        customer = {"status": "INACTIVE"}

        result = customer_activity_status(customer, 5)

        self.assertEqual(result, "INACTIVE_CUSTOMER")


if __name__ == "__main__":
    unittest.main()