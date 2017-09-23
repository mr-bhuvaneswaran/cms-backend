from __future__ import unicode_literals

import datetime
from django.db import models

from management.models import Management


class Batch(models.Model):
    date_of_join = models.DateField(default=datetime.date.today)
    year_of_pass = models.DateField(default=datetime.date.today)

    def __unicode__(self):
        return '{}-{}'.format(self.date_of_join.year, self.year_of_pass.year)


class Department(models.Model):
    name = models.CharField(max_length=127)
    degree = models.CharField(max_length=10)

    def __unicode__(self):
        return '{}-{}'.format(self.degree, self.name)


class ParentsDetail(models.Model):
    father_name = models.CharField(max_length=127)
    mother_name = models.CharField(max_length=127)
    income = models.FloatField(verbose_name="Income")

    def __unicode__(self):
        return '{}'.format(self.father_name)


class MedicalInformation(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    blood_group = models.CharField(max_length=5)
    physically_challenged = models.CharField(max_length=3, choices=(('YES', 'YES'), ('NO', 'NO')))
    eye_colour = models.CharField(max_length=10)
    eye_sight = models.CharField(max_length=10)
    mole = models.CharField(max_length=32)
    scar = models.CharField(max_length=32)

    def __unicode__(self):
        return '{}'.format(self.student.name)


class GeneralInformation(models.Model):
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    religion = models.CharField(max_length=32)
    community = models.CharField(max_length=10)
    caste = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)
    mother_tongue = models.CharField(max_length=32)
    place_of_birth = models.CharField(max_length=32)
    financial_category = models.CharField(max_length=4, choices=(('Self', 'Self'), ('Loan', 'Loan')))
    admission_type = models.CharField(max_length=32)
    admission_category = models.CharField(max_length=32)
    primary_address = models.TextField()
    secondary_address = models.TextField()

    def __unicode__(self):
        return '{}'.format(self.student.name)


class Student(models.Model):
    name=models.CharField(max_length=127)
    roll_no = models.CharField(max_length=127)
    photo = models.ImageField(upload_to="../media", default="../media/default-user-image.png", verbose_name="student_image",name="profile")
    date_of_birth = models.DateField(verbose_name="dob", default=datetime.date.today)
    parent_detail = models.OneToOneField(ParentsDetail, on_delete=models.CASCADE, related_name="student")
    general_information = models.OneToOneField(GeneralInformation, on_delete=models.CASCADE, related_name="student")
    medical_information = models.OneToOneField(MedicalInformation, on_delete=models.CASCADE, related_name="student")
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE, related_name="student")
    department = models.ForeignKey(Department,on_delete=models.CASCADE, related_name="student")
    management = models.ForeignKey(Management, related_name="student")

    def __unicode__(self):
        return '{}-{}'.format(self.name, self.roll_no)


class EducationalInformation(models.Model):
    course = models.CharField(max_length=32)
    institute = models.CharField(max_length=64)
    place = models.CharField(max_length=32)
    percentage = models.FloatField()
    year_of_passedout = models.IntegerField()
    educational_informations = models.ForeignKey(Student, related_name='educational_informations', on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}'.format(self.institute)


class FeesInformation(models.Model):
    paid_fees_amt = models.FloatField()
    balance_fees_amt = models.FloatField()
    student = models.ForeignKey(Student, related_name="fees_information")


    def __unicode__(self):
        return '{}'.format(self.student.name)


class FeesDetail(models.Model):
    name = models.CharField(max_length=32)
    apply_date = models.DateField(default=datetime.date.today)
    due_date = models.DateField(default=datetime.date.today)
    fee_amt = models.FloatField(default=datetime.date.today)
    fees_information = models.OneToOneField(FeesInformation, related_name="fees_detail")

    def __unicode__(self):
        return '{}'.format(self.name)

