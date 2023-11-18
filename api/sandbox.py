
# import requests
# import datetime
# from icalendar import Calendar, Event

# # calendar_url = "https://p153-caldav.icloud.com/published/2/MTc5MzU3MzIzMDcxNzkzNaG6Z3Ra_Rl3HgqLVMldXFhXU5JvskxmKYo96Xd0UMl9iln5yba5LOvkil1X9Xd9Myup2T3LObX7zTdMNNvft1c"
# calendar_url = "https://calendar.google.com/calendar/ical/k8pk9qrn84290s101ss3mn7eqk%40group.calendar.google.com/public/basic.ics"

# calendar_data = requests.get(calendar_url).text
# calendar = Calendar.from_ical(calendar_data)

# for event in calendar.walk("vevent"):
#     print("From: " + str(event.get("dtstart").dt))
#     print("To: " + str(event.get("dtend").dt))
#     print("Summary: " + event.get("summary"))
#     if isinstance(event.get("dtstart").dt, datetime.date) and not isinstance(
#         event.get("dtstart").dt, datetime.datetime
#     ):
#         print("This is an all-day event")
#     else:
#         print("This is not an all-day event")
#     print("------------------")
