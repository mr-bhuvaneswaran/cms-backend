# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models


class Management(models.Model):
    year = models.IntegerField()
    department = models.CharField(max_length=20)

    def __unicode__(self):
        return '{}'.format(self.department, self.year)


class Planner(models.Model):
    name = models.CharField(max_length=32)
    url = models.URLField()
    management = models.ForeignKey(Management,related_name="planner")

    def __unicode__(self):
        return '{}'.format(self.name)


class Event(models.Model):
    name = models.CharField(max_length=64)
    venue = models.CharField(max_length=64)
    date = models.DateField(default=datetime.date.today)
    incharge = models.CharField(max_length=32)
    time = models.CharField(max_length=15)
    phone = models.CharField(max_length=10)
    department = models.CharField(max_length=32)
    description = models.TextField()
    management = models.ForeignKey(Management, related_name="event")

    def __unicode__(self):
        return '{}'.format(self.name)


class Circular(models.Model):
    title = models.CharField(max_length=64)
    date = models.DateField(default=datetime.date.today)
    sender = models.CharField(max_length=64)
    description = models.TextField()
    management = models.ForeignKey(Management, related_name="circular")


    def __unicode__(self):
        return '{}'.format(self.title)






