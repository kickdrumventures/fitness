import datetime
import pytz
from django.utils.timezone import utc

def unix_time(dt):
    epoch = datetime.datetime.utcfromtimestamp(0).replace(tzinfo=utc)
    delta = dt - epoch
    return delta.total_seconds()

def unix_time_millis(dt):
    return unix_time(dt) * 1000.0


