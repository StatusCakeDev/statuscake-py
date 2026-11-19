"""Creates, reads, updates, lists and deletes a pagespeed check."""

import os
import sys

from statuscake import Client, credentials, validation_errors
from statuscake.models import PagespeedTestCheckRate, PagespeedTestRegion


def main() -> None:
    token = os.environ.get("STATUSCAKE_API_TOKEN")
    if not token:
        sys.exit("STATUSCAKE_API_TOKEN not set in environment")

    client = Client(credentials.Bearer(token))

    # A contact group for the check to alert, deleted however the example ends.
    group = client.contact_groups.create_contact_group(name="Development Team")
    group_id = group.data.new_id
    try:
        res = client.pagespeed.create_pagespeed_test(
            name="statuscake.com",
            website_url="https://www.statuscake.com",
            check_rate=PagespeedTestCheckRate.OneDay,
            region=PagespeedTestRegion.UnitedKingdom,
            alert_smaller=10,
            alert_bigger=100,
            alert_slower=1000,
            contact_groups=[group_id],
            paused=True,
        )
        test_id = res.data.new_id
        print(f"PAGESPEED CHECK ID: {test_id}")

        try:
            print("PAGESPEED CHECK:", client.pagespeed.get_pagespeed_test(test_id).data)

            client.pagespeed.update_pagespeed_test(
                test_id,
                check_rate=PagespeedTestCheckRate.OneHour,
                contact_groups=[],  # Remove all contact groups.
                paused=False,
            )
            print("UPDATED PAGESPEED CHECK:", client.pagespeed.get_pagespeed_test(test_id).data)

            print("PAGESPEED CHECKS:", client.pagespeed.list_pagespeed_tests().data)
            print("PAGESPEED CHECK HISTORY:", client.pagespeed.list_pagespeed_test_history(test_id).data)
        finally:
            client.pagespeed.delete_pagespeed_test(test_id)
    finally:
        client.contact_groups.delete_contact_group(group_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report any failure, with the API's reasons if it gave them
        print(e)
        print(validation_errors(e))
        sys.exit(1)
