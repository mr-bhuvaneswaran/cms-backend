# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from student.models import Batch, Department, MedicalInformation, Student,\
                   EducationalInformation, ParentsDetail, GeneralInformation, FeesDetail,\
                   FeesInformation

admin.site.register(Student)
admin.site.register(GeneralInformation)
admin.site.register(MedicalInformation)
admin.site.register(ParentsDetail)
admin.site.register(Department)
admin.site.register(Batch)
admin.site.register(EducationalInformation)
admin.site.register(FeesDetail)
admin.site.register(FeesInformation)