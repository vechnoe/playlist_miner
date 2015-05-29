# coding: utf-8

from celery.task import periodic_task
from celery.schedules import crontab

from miners import data_miner, get_json_from_url, get_feed_from_url, \
    get_date, get_date_from_eastern


@periodic_task(ignore_result=True, run_every=crontab(minute='*/15'))
def kiss_miner_task():
    data_miner(
        'kiss',
        get_json_from_url,
        'song_title',
        'artist',
        'started_at',
        get_date_from_eastern,
        'US/Eastern')

@periodic_task(ignore_result=True, run_every=crontab(minute='*/30'))
def montecarlo_miner_task():
    data_miner(
        'montecarlo',
        get_feed_from_url,
        'song_title',
        'artist',
        'started_at',
        get_date,
        'Europe/Moscow')
