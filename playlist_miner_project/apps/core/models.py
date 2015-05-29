# coding: utf-8

from datetime import datetime, timedelta

from django.db import models

class Radiostation(models.Model):
    name = models.CharField(u'Name', max_length=255)
    url = models.CharField(u'URL', max_length=255)
    data_url = models.CharField(u'Data URL', max_length=500)
    period = models.PositiveIntegerField(
        verbose_name=u'Monitoring period (days)',
        default=7
    )

    def __unicode__(self):
        return u'%s | %s' % (self.name, self.url)

    class Meta:
        verbose_name = u'Radiostation'
        verbose_name_plural = u'Radiostations'


class Song(models.Model):
    radiostation = models.ForeignKey(Radiostation)
    title = models.CharField(u'Song title', max_length=255)
    artist = models.CharField(u'Artist', max_length=255)

    def __unicode__(self):
        return u'%s | %s' % (self.title, self.artist)

    def _get_period(self):
        """
        It returns monitoring period
        """
        now_date = datetime.utcnow()
        begin_date = now_date - timedelta(self.radiostation.period)
        return begin_date, now_date + timedelta(1)

    def _get_airplay_period(self):
        """
        It returns queryset from monitorig period
        """
        return self.airplay_set.filter(
            date__range=(self._get_period()))

    def get_airplay_count(self):
        """
        Total airplay's quantity from monitorig period
        """
        return self._get_airplay_period().count()

    def get_chart_dynamic(self):
        """
        Dynamic playbacks, according daily airplay count
        """
        yesterday = datetime.utcnow() - timedelta(1)
        yesterday_airplay_count = self._get_airplay_period().filter(
            date__day=yesterday.day,
            date__month=yesterday.month,
            date__year=yesterday.year
        ).count()
        daily_airplay_count = self._get_airplay_period().filter(
            date__day=datetime.utcnow().day,
            date__month=datetime.utcnow().month,
            date__year=datetime.utcnow().year
        ).count()

        index = 0
        if yesterday_airplay_count == daily_airplay_count:
            index = 0
        elif daily_airplay_count < yesterday_airplay_count:
            index = -1
        elif daily_airplay_count > yesterday_airplay_count:
            index = 1

        return index

    def is_chart_hit(self):
        """
        The song becomes a hit, when daily airplay count > 4
        """
        daily_airplay_count = self._get_airplay_period().filter(
            date__day=datetime.utcnow().day,
            date__month=datetime.utcnow().month,
            date__year=datetime.utcnow().year
        ).count()
        if daily_airplay_count >= 4:
            return True
        return False

    class Meta:
        verbose_name = u'Song'
        verbose_name_plural = u'Songs'


class Airplay(models.Model):
    radiostation = models.ForeignKey(Radiostation)
    song = models.ForeignKey(Song)
    date = models.DateTimeField(u'Date of airplay', blank=True, null=True)

    def __unicode__(self):
        return u'%s | %s' % (self.song, self.date)

    class Meta:
        ordering = ['-date']
        verbose_name = u'Airplay'
        verbose_name_plural = u'Airplays'
