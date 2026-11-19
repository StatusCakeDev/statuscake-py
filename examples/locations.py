"""Lists the locations that checks can run from."""

import os
import sys

from statuscake import Client, credentials, validation_errors


def main() -> None:
    token = os.environ.get("STATUSCAKE_API_TOKEN")
    if not token:
        sys.exit("STATUSCAKE_API_TOKEN not set in environment")

    client = Client(credentials.Bearer(token))

    print("PAGESPEED LOCATIONS:", client.locations.list_pagespeed_monitoring_locations().data)

    # The region codes are the values that an uptime check accepts as regions.
    print("UPTIME LOCATIONS:", client.locations.list_uptime_monitoring_locations().data)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report any failure, with the API's reasons if it gave them
        print(e)
        print(validation_errors(e))
        sys.exit(1)
