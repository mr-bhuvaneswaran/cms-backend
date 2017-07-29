from __future__ import unicode_literals

from django.db import models



class Batch(models.Model):
    date_of_join = models.DateField()
    year_of_pass = models.DateField()

    def __unicode__(self):
        return '{}-{}'.format(self.date_of_join.year, self.year_of_pass.unique_for_year)


class Department(models.Model):
    name = models.CharField(max_length=127)
    degree = models.CharField(max_length=10)

    def __unicode__(self):
        return '{}-{}'.format(self.name, self.degree)


class ParentDetails(models.Model):
    father_name = models.CharField(max_length=127)
    mother_name = models.CharField(max_length=127)
    income = models.FloatField(verbose_name="Income")

    def __unicode__(self):
        return '{}'.format(self.father_name)

class MedicalInformation(models.Model):
    height = models.FloatField()
    weight = models.FloatField()
    blood_group = models.CharField(max_length=5)
    physically_challenged = models.CharField(max_length=3,choices=(('YES','YES'),('NO','NO')))
    eye_colour = models.CharField(max_length=10)
    eye_sight = models.CharField(max_length=10)
    mole = models.CharField(max_length=32)
    scar = models.CharField(max_length=32)

    def __unicode__(self):
        return '{}-{}'.format("Medical Information",self.blood_group)

class PersonalDetails(models.Model):
    date_of_birth = models.DateField(verbose_name="dob")
    gender = models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female'),('Other','Other')))
    religion = models.CharField(max_length=32)
    community =models.CharField(max_length=10)
    caste = models.CharField(max_length=32)
    nationality = models.CharField(max_length=32)
    mother_tongue = models.CharField(max_length=32)
    place_of_birth = models.CharField(max_length=32)
    financial_category = models.CharField(max_length=4,choices=(('Self','Self'),('Loan','Loan')))
    admission_type = models.CharField(max_length=32)
    admission_category = models.CharField(max_length=32)
    primary_address = models.TextField()
    secondary_address = models.TextField()

    def __unicode__(self):
        return '{}-{}'.format("Personal Details", self.gender)

class Student(models.Model):
    name=models.CharField(max_length=127)
    roll_no = models.CharField(max_length=127)
    profile = models.OneToOneField(PersonalDetails,on_delete=models.CASCADE)
    parent = models.OneToOneField(ParentDetails,on_delete=models.CASCADE)
    batch = models.OneToOneField(Batch, on_delete=models.CASCADE)
    department = models.OneToOneField(Department,on_delete=models.CASCADE)
    medical_information = models.OneToOneField(MedicalInformation,on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}-{}'.format(self.name, self.roll_no)


class EducationalInformations(models.Model):
    course = models.CharField(max_length=32)
    institute = models.CharField(max_length=64)
    place = models.CharField(max_length=32)
    percentage = models.FloatField()
    year_of_passedout = models.IntegerField()
    educational_informations = models.ForeignKey(Student, related_name='educational_informations', on_delete=models.CASCADE)

    def __unicode__(self):
        return '{}-{}'.format(self.course, self.percentage)


