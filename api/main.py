from typing import Union
from fastapi import FastAPI
from datetime import datetime, timedelta
import os
from . import ical

api = FastAPI()


@api.get("/events")
def get_events(
    url: Union[str, None] = None,
    mode: Union[str, None] = None,
    days: Union[int, None] = None,
    eventsFrom: Union[str, None] = None,
    eventsTo: Union[str, None] = None,
):
    if url is None:
        if os.environ.get("ICAL_URL") is not None:
            url = os.environ.get("ICAL_URL")
        else:
            return {"error": "No URL provided"}
    if mode is None:
        mode = "today"
    if (mode == "range") and (eventsFrom is not None) and (eventsTo is not None):
        return ical.get_events(url, eventsFrom, eventsTo)
    if mode == "today":
        today = datetime.today().strftime("%Y-%m-%d")
        return ical.get_events(url, today, today)
    if (mode == "days") and (days is not None):
        today = datetime.today().strftime("%Y-%m-%d")
        end = (datetime.today() + timedelta(days=days)).strftime("%Y-%m-%d")
        return ical.get_events(url, today, end)
    else:
        return {"error": "Invalid parameters"}
