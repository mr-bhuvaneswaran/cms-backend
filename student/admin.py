# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from student.models import EducationalInformations, Batch, Department, ParentDetails, MedicalInformation, \
    PersonalDetails, Student

admin.site.register(Student)
admin.site.register(PersonalDetails)
admin.site.register(MedicalInformation)
admin.site.register(ParentDetails)
admin.site.register(Department)
admin.site.register(Batch)
admin.site.register(EducationalInformations)