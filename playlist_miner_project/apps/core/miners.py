# coding: utf-8

import re
import json
import urllib
import datetime

import pytz
import feedparser
from dateutil import parser

from django.db.models import Q

from core.models import Radiostation, Song, Airplay


def get_json_from_url(url):
    """
    It returns python dict.
    """
    response = urllib.urlopen(url)
    if response.code == 200:
        data = json.loads(response.read())
        return data
    return []

def get_feed_from_url(url):
    """
    Xml rss fedd parser
    """
    feed = feedparser.parse(url)
    # removing date from feed
    for item in feed.entries:
        item['description'] = re.sub(
            r'\d{1,2}:\d{1,2}', '', item['description'])

    out = []
    # removing <a> links from feed
    for item in feed.entries:
        content = re.sub(r'<[^>]*>', '', item['description']).split(' - ')
        out.append(
            dict(
                artist=content[0].lstrip(),
                song_title=content[1],
                started_at=item.get('published')
            )
        )
    return out

def get_date(date_from_string, timezone):
    """
    It returns date in UTC from string
    """
    tz = pytz.timezone(timezone)
    date_in = parser.parse(date_from_string)

    try:
        return tz.normalize(tz.localize(date_in)).astimezone(pytz.utc)
    except ValueError:
        return date_in.astimezone(pytz.utc)

def get_date_from_eastern(date_from_string, timezone):
    """
    It returns date in UTC from string with format "11:24 am",
    local time must be in UTC, input timezone must be is 'US/Eastern'
    """
    tz = pytz.timezone(timezone)
    date = parser.parse(date_from_string)
    if date.hour > 20:
        date = date - datetime.timedelta(1)
    return tz.normalize(tz.localize(date)).astimezone(pytz.utc)


def data_miner(
        radiostation_name, function_parser,
        song_title_field, artist_field, date_field, date_handler, timeznone):
    """
    Handle data from parser and saving it to DB.

    :param radiostation_name: string, e.g.: 'montecarlo'
    :param function_parser: variable, e.g.: get_json_from_url
    :param song_title_field: string, e.g.: 'song_title'
    :param artist_field: string, e.g.: 'artist'
    :param date_field: string, e.g.: 'published'
    :param date_handler: variable, e.g.: get_date
    :param timeznone: string, e.g.: 'US/Eastern'
    """
    station = Radiostation.objects.filter(
        name__icontains=radiostation_name).first()
    data = function_parser(station.data_url)
    if len(data) > 0:
        for item in data:
            song = Song.objects.filter(
                Q(title__icontains=item.get(song_title_field)) &
                Q(artist__icontains=item.get(artist_field))
            )
            airplay_date = date_handler(item.get(date_field), timeznone)
            airplay = Airplay.objects.filter(date=airplay_date)
            if not song.exists():
                newsong = Song()
                newsong.radiostation = station
                newsong.title = item.get(song_title_field)
                newsong.artist = item.get(artist_field)
                newsong.save()
                if not airplay.exists():
                    newairplay = Airplay()
                    newairplay.radiostation = station
                    newairplay.song = newsong
                    newairplay.date = airplay_date
                    newairplay.save()
            elif song.exists():
                if not airplay.exists():
                    newairplay = Airplay()
                    newairplay.radiostation = station
                    newairplay.song = song.first()
                    newairplay.date = airplay_date
                    newairplay.save()
        print '%s Paser done' % station.name
    else:
        print '%s Paser failed' % station.name




