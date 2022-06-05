import events
import pushover
import os

events.download_events(os.getenv('EVENTS_URL'))

events_list = events.read_events()
for event in events_list:
    pushover.send_notification(
        event['notification']['title'],
        event['notification']['message'],
    )
