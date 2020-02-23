from datetime import datetime, timedelta, timezone
import json
from test import find_latest, db, update_status_ram, update_status_hdd

find_latest(db,"Cendana",'Washer_1')
update_status_ram(db,"Cendana", "Washer_1", "AVAILABLE", strftime(datetime.now()))
update_status_hdd()
print(find_latest.time, find_latest.status)