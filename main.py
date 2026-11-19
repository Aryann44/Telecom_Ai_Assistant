from agent.agent_controller import TelecomAgent


def main():

    print("=" * 55)

    print("     TELECOM AI TROUBLESHOOTING ASSISTANT")

    print("=" * 55)

    customer_id = input("\nEnter Customer ID: ").strip().upper()

    complaint = input(

        "Describe the customer issue: "

    ).strip()

    if not customer_id or not complaint:

        print("\nCustomer ID and complaint are required.")

        return

    agent = TelecomAgent()

    result = agent.troubleshoot(

        customer_id,

        complaint

    )

    print("\n" + "=" * 55)

    print("           TROUBLESHOOTING REPORT")

    print("=" * 55)

    if result.get("status") == "FAILED":

        print("\nError:", result["message"])

        return

    print("\nCustomer ID:", result["customer_id"])

    print("Complaint:", result["complaint"])

    print("\n--- SYSTEM STATUS ---")

    print("Account:", result["account_status"])

    print("Service:", result["service_status"])

    print("Network:", result["network_status"])

    print("Router:", result["router_status"])

    print("\n--- DIAGNOSIS ---")

    for finding in result["findings"]:

        print("-", finding)

    print("\n--- RECOMMENDATION ---")

    print(result["recommendation"])

    print("\nPriority:", result["priority"])

    print("\n" + "=" * 55)


if __name__ == "__main__":

    main()
    
