import csv
import logging

logger = logging.getLogger(__name__)

def load_customers(file_path):
    customers = {}

    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                customers[row["customer_id"]] = row

    except Exception as e:
        logger.error(f"Error loading customers file: {e}")

    return customers


def load_orders(file_path):
    orders = []

    try:
        with open(file_path, mode='r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                orders.append(row)

    except Exception as e:
        logger.error(f"Error loading orders file: {e}")

    return orders