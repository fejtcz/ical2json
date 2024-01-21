import requests
import requests_cache
from cleantext import clean
from icalendar import Calendar
from datetime import datetime, timedelta

date_format_ical = "%Y-%m-%d %H:%M:%S"
date_format_api = "%Y-%m-%d"


def get_ical_data(url):
    requests_cache.install_cache('calendar')
    data = requests.get("https://" + url)
    if data.status_code == 200:
        return str(data.text)
    else:
        return False


def clean_text(string):
    return clean(string, lower=False, no_line_breaks=True, no_urls=True)


def get_events(url, events_from, events_end):
    calendar_data = get_ical_data(url)
    if calendar_data:
        events = []
        calendar = Calendar.from_ical(calendar_data)
        start_from = datetime.strptime(events_from, date_format_api)
        end_to = datetime.strptime(events_end, date_format_api)

        for event in calendar.walk("vevent"):
            event_start = datetime.strptime(
                event.get("dtstart").dt.strftime(date_format_ical), date_format_ical
            )
            event_end = datetime.strptime(
                event.get("dtend").dt.strftime(date_format_ical), date_format_ical
            )

            if (event_start >= start_from and event_start < end_to + timedelta(days=1)) or ((event_end > start_from) and (event_end <= end_to + timedelta(days=1))) or ((event_start < start_from) and (event_end > end_to)):
                events.append(
                    {
                        "summary": clean_text(event.get("summary")),
                        "description": clean_text(event.get("description")),
                        "location": clean_text(event.get("location")),
                        "start_ical": str(event_start),
                        "start_timestamp": int(event_start.timestamp()),
                        "end_ical": str(event_end),
                        "end_timestamp": int(event_end.timestamp()),
                    }
                )
        return sorted(events, key=lambda dct: dct["start_ical"])
    else:
        return {"error": "No iCal data found"}
