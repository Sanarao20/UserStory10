import unittest
from src.order_processor import aggregate_orders, is_valid_order


class TestOrderProcessor(unittest.TestCase):

    def test_customer_order_aggregation(self):

        customers = {"1": {"status": "ACTIVE"}}

        orders = [{
            "customer_id": "1",
            "order_date": "2024-05-10",
            "order_amount": "1000",
            "order_status": "DELIVERED"
        }]

        result = aggregate_orders(customers, orders)

        self.assertEqual(result["1"]["total_orders"], 1)

    def test_invalid_order_date_ignored(self):

        order = {
            "order_date": "invalid",
            "order_amount": "100",
        }

        self.assertFalse(is_valid_order(order))

    def test_negative_order_amount_ignored(self):

        order = {
            "order_date": "2024-05-10",
            "order_amount": "-100"
        }

        self.assertFalse(is_valid_order(order))


if __name__ == "__main__":
    unittest.main()