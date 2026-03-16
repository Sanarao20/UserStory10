import logging
import os
from pathlib import Path
from loader import load_customers, load_orders
from order_processor import aggregate_orders
from loyalty_engine import classify_loyalty, customer_activity_status
from reporter import generate_customer_report, generate_summary

BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data"
LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_DIR / "analytics.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():

    logger.info("Customer Analytics Engine Started")

    customers_file = DATA_DIR / "customers.csv"
    orders_file = DATA_DIR / "orders.csv"

    customers = load_customers(customers_file)
    orders = load_orders(orders_file)

    logger.info("Data loaded successfully")

    metrics = aggregate_orders(customers, orders)

    logger.info("Order aggregation completed")

    generate_customer_report(
        customers,
        metrics,
        classify_loyalty,
        customer_activity_status,
        BASE_DIR / "customer_loyalty_report.csv"
    )

    generate_summary(
        customers,
        metrics,
        classify_loyalty,
        customer_activity_status,
        BASE_DIR / "analytics_summary.json"
    )

    logger.info("Reports generated successfully")
    logger.info("Customer Analytics Engine Completed")


if __name__ == "__main__":
    main()