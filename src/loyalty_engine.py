def classify_loyalty(total_spent):

    if total_spent >= 10000:
        return "PLATINUM"
    elif total_spent >= 5000:
        return "GOLD"
    elif total_spent >= 1000:
        return "SILVER"
    else:
        return "BRONZE"


def customer_activity_status(customer, total_orders):

    if customer["status"] == "INACTIVE":
        return "INACTIVE_CUSTOMER"

    if customer["status"] == "ACTIVE" and total_orders == 0:
        return "INACTIVE_CUSTOMER"

    return "ACTIVE_CUSTOMER"