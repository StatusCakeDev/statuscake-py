"""Creates, reads, updates, lists and deletes a contact group."""

import os
import sys

from statuscake import Client, credentials, validation_errors


def main() -> None:
    token = os.environ.get("STATUSCAKE_API_TOKEN")
    if not token:
        sys.exit("STATUSCAKE_API_TOKEN not set in environment")

    client = Client(credentials.Bearer(token))

    res = client.contact_groups.create_contact_group(
        name="Operations Team",
        email_addresses=["johnsmith@example.com", "janesmith@example.com"],
        integrations=["1", "2", "3"],
        mobile_numbers=["447712345678", "447987462344"],
        ping_url="https://ping.example.com",
    )
    group_id = res.data.new_id
    print(f"CONTACT GROUP ID: {group_id}")

    # The group is deleted however the rest of the example ends.
    try:
        print("CONTACT GROUP:", client.contact_groups.get_contact_group(group_id).data)

        client.contact_groups.update_contact_group(
            group_id,
            name="Development Team",
            email_addresses=[],  # Remove all email addresses.
            integrations=["4", "5", "6"],
            mobile_numbers=["447891998195"],
            ping_url="https://ping.example.com/groups",
        )
        print("UPDATED CONTACT GROUP:", client.contact_groups.get_contact_group(group_id).data)

        print("CONTACT GROUPS:", client.contact_groups.list_contact_groups().data)
    finally:
        client.contact_groups.delete_contact_group(group_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report any failure, with the API's reasons if it gave them
        print(e)
        print(validation_errors(e))
        sys.exit(1)
