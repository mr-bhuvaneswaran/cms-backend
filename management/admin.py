# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from management.models import Management, Planner, Event, Circular

admin.site.register(Management)
admin.site.register(Circular)
admin.site.register(Event)
admin.site.register(Planner)
