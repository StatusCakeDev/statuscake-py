
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.contact_groups_api import ContactGroupsApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from statuscake.api.contact_groups_api import ContactGroupsApi
from statuscake.api.heartbeat_api import HeartbeatApi
from statuscake.api.locations_api import LocationsApi
from statuscake.api.maintenance_windows_api import MaintenanceWindowsApi
from statuscake.api.pagespeed_api import PagespeedApi
from statuscake.api.ssl_api import SslApi
from statuscake.api.uptime_api import UptimeApi
