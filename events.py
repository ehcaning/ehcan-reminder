import datetime
import yaml
import urllib.request as req


def download_events(url):
    req.urlretrieve(url, "events.yaml")


def read_events(event_name="events.yaml"):
    with open(event_name, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
        return data_loaded['events']


def is_time_for_remind(original_date, remind_on, today=None):
    if today is None:
        today = datetime.date.today()

    date_to_compare = original_date.replace(year=today.year)
    for days_before in remind_on:
        d = date_to_compare + datetime.timedelta(days=days_before)
        if d == today:
            return True

    return False
