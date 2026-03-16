from datetime import datetime
import logging

logger = logging.getLogger(__name__)

TARGET_MONTH = 5
TARGET_YEAR = 2024


def is_valid_order(order):

    try:
        order_date = datetime.strptime(order["order_date"], "%Y-%m-%d")

        if order_date.year != TARGET_YEAR or order_date.month != TARGET_MONTH:
            return False

    except Exception:
        logger.warning(f"Invalid date skipped: {order}")
        return False

    try:
        amount = float(order["order_amount"])
        if amount < 0:
            logger.warning("Negative amount ignored")
            return False
    except Exception:
        return False

    return True


def aggregate_orders(customers, orders):

    metrics = {}

    for cid in customers:
        metrics[cid] = {
            "total_orders": 0,
            "total_spent": 0.0
        }

    for order in orders:

        if not is_valid_order(order):
            continue

        cid = order["customer_id"]

        if cid not in customers:
            logger.warning(f"Unknown customer id: {cid}")
            continue

        if order["order_status"] != "DELIVERED":
            continue

        amount = float(order["order_amount"])

        metrics[cid]["total_orders"] += 1
        metrics[cid]["total_spent"] += amount

    for cid in metrics:
        orders = metrics[cid]["total_orders"]

        if orders == 0:
            avg = 0
        else:
            avg = metrics[cid]["total_spent"] / orders

        metrics[cid]["average_order_value"] = round(avg, 2)

    return metrics