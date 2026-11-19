"""Creates, reads, updates, lists and deletes a maintenance window."""

import os
import sys
from datetime import datetime, timedelta, timezone

from statuscake import Client, credentials, validation_errors
from statuscake.models import MaintenanceWindowRepeatInterval


def main() -> None:
    token = os.environ.get("STATUSCAKE_API_TOKEN")
    if not token:
        sys.exit("STATUSCAKE_API_TOKEN not set in environment")

    client = Client(credentials.Bearer(token))

    now = datetime.now(timezone.utc)

    res = client.maintenance_windows.create_maintenance_window(
        name="Weekly maintenance",
        start_at=now,
        end_at=now + timedelta(hours=3),
        repeat_interval=MaintenanceWindowRepeatInterval.Weekly,
        tags=["testing"],
        timezone="UTC",
    )
    window_id = res.data.new_id
    print(f"MAINTENANCE WINDOW ID: {window_id}")

    try:
        print("MAINTENANCE WINDOW:", client.maintenance_windows.get_maintenance_window(window_id).data)

        client.maintenance_windows.update_maintenance_window(
            window_id,
            name="Monthly maintenance",
            start_at=now,
            end_at=now + timedelta(hours=48),
            repeat_interval=MaintenanceWindowRepeatInterval.Monthly,
        )
        print("UPDATED MAINTENANCE WINDOW:", client.maintenance_windows.get_maintenance_window(window_id).data)

        print("MAINTENANCE WINDOWS:", client.maintenance_windows.list_maintenance_windows().data)
    finally:
        client.maintenance_windows.delete_maintenance_window(window_id)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:  # noqa: BLE001 - report any failure, with the API's reasons if it gave them
        print(e)
        print(validation_errors(e))
        sys.exit(1)
