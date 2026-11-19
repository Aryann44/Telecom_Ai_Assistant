from tools.telecom_tools import (

    check_account_status,

    check_service_status,

    check_network_status,

    check_router_status

)


class TelecomAgent:

    def troubleshoot(self, customer_id, complaint):

        print("\n[AGENT] Starting troubleshooting...")

        print("[AGENT] Customer ID:", customer_id)

        # Step 1: Check customer account

        account = check_account_status(customer_id)

        if "error" in account:

            return {

                "status": "FAILED",

                "message": account["error"]

            }

        print("[TOOL] Account check completed.")

        # Step 2: Check broadband service

        service = check_service_status(customer_id)

        print("[TOOL] Service check completed.")

        # Step 3: Check network availability

        network = check_network_status(customer_id)

        print("[TOOL] Network check completed.")

        # Step 4: Check router status

        router = check_router_status(customer_id)

        print("[TOOL] Router check completed.")

        # Step 5: Analyse results

        findings = []

        if account["account_status"] != "ACTIVE":

            findings.append("Customer account is not active.")

        if service["service_status"] != "ACTIVE":

            findings.append("Broadband service is inactive.")

        if network["network_status"] == "OUTAGE":

            findings.append("A network outage is detected.")

        if router["router_status"] == "OFFLINE":

            findings.append("Customer router is offline.")

        if findings:

            diagnosis = findings

            recommendation = (

                "Investigate the identified issue "

                "before restoring the service."

            )

            priority = "HIGH"

        else:

            diagnosis = ["No fault detected in the available checks."]

            recommendation = (

                "Perform additional diagnostics and "

                "verify the customer's physical connection."

            )

            priority = "MEDIUM"

        # Step 6: Return final report

        return {

            "customer_id": customer_id,

            "complaint": complaint,

            "account_status": account["account_status"],

            "service_status": service["service_status"],

            "network_status": network["network_status"],

            "router_status": router["router_status"],

            "findings": diagnosis,

            "recommendation": recommendation,

            "priority": priority

        }
 