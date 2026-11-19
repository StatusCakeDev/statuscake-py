"""Creates, reads, updates, lists and deletes an uptime check."""

import os
import sys

from statuscake import Client, credentials, validation_errors
from statuscake.models import UptimeTestCheckRate, UptimeTestType


def main() -> None:
    token = os.environ.get("STATUSCAKE_API_TOKEN")
    if not token:
        sys.exit("STATUSCAKE_API_TOKEN not set in environment")

    client = Client(credentials.Bearer(token))

    # A contact group for the check to alert, deleted however the example ends.
    group = client.contact_groups.create_contact_group(name="Development Team")
    group_id = group.data.new_id
    try:
        res = client.uptime.create_uptime_test(
            name="statuscake.com",
            test_type=UptimeTestType.HTTP,
            website_url="https://www.statuscake.com",
            check_rate=UptimeTestCheckRate.FifteenMinutes,
            contact_groups=[group_id],
            enable_ssl_alert=True,
            follow_redirects=True,
            paused=True,
            regions=["london"],
            tags=["testing"],
        )
        test_id = res.data.new_id
        print(f"UPTIME CHECK ID: {test_id}")

        try:
            print("UPTIME CHECK:", client.uptime.get_uptime_test(test_id).data)

            client.uptime.update_uptime_test(
                test_id,
                check_rate=UptimeTestCheckRate.ThirtyMinutes,
                paused=False,
                regions=["london", "paris"],
            )
            print("UPDATED UPTIME CHECK:", client.uptime.get_uptime_test(test_id).data)

            print("UPTIME CHECKS:", client.uptime.list_uptime_tests().data)
            print("UPTIME CHECK HISTORY:", client.uptime.list_uptime_test_history(test_id).data)
            print("UPTIME CHECK PERIODS:", client.uptime.list_uptime_test_periods(test_id).data)
            print("SENT ALERTS:", client.uptime.list_uptime_test_alerts(test_id).data)
        finally:
            client.uptime.delete_uptime_test(test_id)
    finally:
        client.contact_groups.delete_contact_group(group_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report any failure, with the API's reasons if it gave them
        print(e)
        print(validation_errors(e))
        sys.exit(1)
