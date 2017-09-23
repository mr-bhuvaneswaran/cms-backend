# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from academics.models import Academic, LibraryStatus, WorkingMonth, Attendance, SemesterSubject, ExamResult, \
    InternalExamSubject, InternalExam, InternalMarkDetail

admin.site.register(Academic)
admin.site.register(LibraryStatus)
admin.site.register(InternalMarkDetail)
admin.site.register(InternalExam)
admin.site.register(InternalExamSubject)
admin.site.register(ExamResult)
admin.site.register(SemesterSubject)
admin.site.register(Attendance)
admin.site.register(WorkingMonth)
