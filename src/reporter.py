import csv
import json


def generate_customer_report(customers, metrics, classify_func, activity_func, file_path):

    rows = []

    for cid, customer in customers.items():

        data = metrics[cid]

        loyalty = classify_func(data["total_spent"])

        activity = activity_func(customer, data["total_orders"])

        rows.append({
            "customer_id": cid,
            "customer_name": customer["customer_name"],
            "total_orders": data["total_orders"],
            "total_spent": data["total_spent"],
            "average_order_value": data["average_order_value"],
            "loyalty_segment": loyalty,
            "customer_activity_status": activity
        })

    if not rows:
        return

    with open(file_path, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def generate_summary(customers, metrics, classify_func, activity_func, file_path):

    summary = {
        "total_customers": len(customers),
        "active_customers": 0,
        "inactive_customers": 0,
        "platinum_customers": 0,
        "gold_customers": 0,
        "silver_customers": 0,
        "bronze_customers": 0,
        "total_revenue": 0
    }

    for cid, customer in customers.items():

        spent = metrics[cid]["total_spent"]
        total_orders = metrics[cid]["total_orders"]

        segment = classify_func(spent)

        activity = activity_func(customer, total_orders)

        summary["total_revenue"] += spent

        # Loyalty segmentation
        if segment == "PLATINUM":
            summary["platinum_customers"] += 1
        elif segment == "GOLD":
            summary["gold_customers"] += 1
        elif segment == "SILVER":
            summary["silver_customers"] += 1
        else:
            summary["bronze_customers"] += 1

        # Activity status count
        if activity == "ACTIVE_CUSTOMER":
            summary["active_customers"] += 1
        else:
            summary["inactive_customers"] += 1

    with open(file_path, "w") as file:
        json.dump(summary, file, indent=4)