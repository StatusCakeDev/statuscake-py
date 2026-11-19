"""Creates, reads, updates, lists and deletes a heartbeat check."""

import os
import sys

from statuscake import Client, credentials, validation_errors


def main() -> None:
    token = os.environ.get("STATUSCAKE_API_TOKEN")
    if not token:
        sys.exit("STATUSCAKE_API_TOKEN not set in environment")

    client = Client(credentials.Bearer(token))

    # A contact group for the check to alert, deleted however the example ends.
    group = client.contact_groups.create_contact_group(name="Development Team")
    group_id = group.data.new_id
    try:
        res = client.heartbeat.create_heartbeat_test(
            name="statuscake.com",
            period=1800,
            contact_groups=[group_id],
            paused=True,
            tags=["testing"],
        )
        test_id = res.data.new_id
        print(f"HEARTBEAT CHECK ID: {test_id}")

        try:
            print("HEARTBEAT CHECK:", client.heartbeat.get_heartbeat_test(test_id).data)

            client.heartbeat.update_heartbeat_test(test_id, period=3600, paused=False)
            print("UPDATED HEARTBEAT CHECK:", client.heartbeat.get_heartbeat_test(test_id).data)

            print("HEARTBEAT CHECKS:", client.heartbeat.list_heartbeat_tests().data)
        finally:
            client.heartbeat.delete_heartbeat_test(test_id)
    finally:
        client.contact_groups.delete_contact_group(group_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report any failure, with the API's reasons if it gave them
        print(e)
        print(validation_errors(e))
        sys.exit(1)
