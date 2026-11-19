import json

from pathlib import Path

# Locate the telecom data file

DATA_FILE = (

    Path(__file__).resolve().parent.parent

    / "data"

    / "telecom_data.json"

)


def load_telecom_data():

    """Load simulated telecom customer data."""

    with open(DATA_FILE, "r", encoding="utf-8") as file:

        return json.load(file)


def get_customer_details(customer_id):

    """Find a customer using customer ID."""

    data = load_telecom_data()

    for customer in data["customers"]:

        if customer["customer_id"] == customer_id:

            return customer

    return None


def check_account_status(customer_id):

    """Check whether the customer account is active."""

    customer = get_customer_details(customer_id)

    if customer is None:

        return {"error": "Customer not found"}

    return {

        "customer_id": customer_id,

        "account_status": customer["account_status"]

    }


def check_service_status(customer_id):

    """Check broadband service status."""

    customer = get_customer_details(customer_id)

    if customer is None:

        return {"error": "Customer not found"}

    return {

        "customer_id": customer_id,

        "service_status": customer["service_status"],

        "service_type": customer["service_type"]

    }


def check_network_status(customer_id):

    """Check network availability."""

    customer = get_customer_details(customer_id)

    if customer is None:

        return {"error": "Customer not found"}

    return {

        "customer_id": customer_id,

        "network_status": customer["network_status"]

    }


def check_router_status(customer_id):

    """Check customer router/CPE status."""

    customer = get_customer_details(customer_id)

    if customer is None:

        return {"error": "Customer not found"}

    return {

        "customer_id": customer_id,

        "router_status": customer["router_status"]

    }

     
 