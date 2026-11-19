"""Creates, reads, updates, lists and deletes an SSL check."""

import os
import sys

from statuscake import Client, credentials, validation_errors
from statuscake.models import SSLTestCheckRate


def main() -> None:
    token = os.environ.get("STATUSCAKE_API_TOKEN")
    if not token:
        sys.exit("STATUSCAKE_API_TOKEN not set in environment")

    client = Client(credentials.Bearer(token))

    # A contact group for the check to alert, deleted however the example ends.
    group = client.contact_groups.create_contact_group(name="Development Team")
    group_id = group.data.new_id
    try:
        res = client.ssl.create_ssl_test(
            website_url="https://www.statuscake.com",
            check_rate=SSLTestCheckRate.FiveMinutes,
            alert_at=[1, 7, 30],
            alert_broken=True,
            alert_expiry=True,
            alert_mixed=True,
            alert_reminder=True,
            contact_groups=[group_id],
            follow_redirects=True,
            paused=True,
        )
        test_id = res.data.new_id
        print(f"SSL CHECK ID: {test_id}")

        try:
            print("SSL CHECK:", client.ssl.get_ssl_test(test_id).data)

            client.ssl.update_ssl_test(
                test_id,
                check_rate=SSLTestCheckRate.OneHour,
                contact_groups=[],  # Remove all contact groups.
                paused=False,
            )
            print("UPDATED SSL CHECK:", client.ssl.get_ssl_test(test_id).data)

            print("SSL CHECKS:", client.ssl.list_ssl_tests().data)
        finally:
            client.ssl.delete_ssl_test(test_id)
    finally:
        client.contact_groups.delete_contact_group(group_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report any failure, with the API's reasons if it gave them
        print(e)
        print(validation_errors(e))
        sys.exit(1)
