from dateutil.parser import isoparse, parse
from dateutil.tz import UTC
import pytz


d = isoparse("2024-03-06T19:45:00+00:00").replace(tzinfo=None)
print(d)

# print(d.astimezone(UTC))
# print((pytz.timezone('Europe/Moscow').localize(d)))
