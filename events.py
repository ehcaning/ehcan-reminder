import yaml
import urllib.request as req


def download_events(url):
    req.urlretrieve(url, "events.yaml")


def read_events():
    with open("events.yaml", 'r') as stream:
        data_loaded = yaml.safe_load(stream)
        return data_loaded['events']
