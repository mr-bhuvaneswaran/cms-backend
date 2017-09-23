# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models

from student.models import Student


class Academic(models.Model):
    semester = models.IntegerField()
    student = models.ForeignKey(Student, related_name="academic")

    # feedback = models.ForeignKey(Feedback)

    def __unicode__(self):
        return '{}-sem-{}'.format(self.student.name, self.semester)


class Attendance(models.Model):
    percentage = models.FloatField()
    academics = models.ForeignKey(Academic, related_name="attendance")

    def __unicode__(self):
        return '{}-{}%'.format(self.academics.student.name, self.percentage)


class WorkingMonth(models.Model):
    month = models.CharField(max_length=20, choices=(('JANUARY', 'JANUARY'), ('FEBRUARY', 'FEBRUARY')
                                                     , ('MARCH', 'MARCH'), ('APRIL', 'APRIL'), ('MAY', 'MAY'),
                                                     ('JUNE', 'JUNE'), ('JULY', 'JULY'), ('AUGUST', 'AUGUST'),
                                                     ('SEPTEMBER', 'SEPTEMBER'), ('OCTOBER', 'OCTOBER'),
                                                     ('NOVEMBER', 'NOVEMBER'), ('DECEMBER', 'DECEMBER')))
    year = models.IntegerField()
    attendance = models.OneToOneField(Attendance, on_delete= models.CASCADE, related_name="working_month")

    def __unicode__(self):
        return '{}-{}'.format(self.month, self.year)


class ExamResult(models.Model):
    academics = models.OneToOneField(Academic, related_name="exam_results", primary_key=True)
    cgpa = models.FloatField(default=0.0)
    gpa = models.FloatField(default=0.0)

    def __unicode__(self):
        return '{}-sem-{}'.format(self.academics.student.name, self.academics.semester)


class SemesterSubject(models.Model):
    sem_no = models.IntegerField()
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=50)
    grade = models.CharField(max_length=4)
    grade_point = models.IntegerField()
    credit_point = models.IntegerField()
    status = models.CharField(max_length=5, choices=(("Pass","Pass"), ("Fail", "Fail")))
    exam_result = models.ForeignKey(ExamResult, related_name="semester_subject")

    def __unicode__(self):
        return '{}'.format(self.subject_code)


# class Feedback(models.Model):
#
#     def __unicode__(self):
#         return '{}'.format(self)


class InternalMarkDetail(models.Model):
    academics = models.OneToOneField(Academic, related_name="internal_mark_detail")

    def __unicode__(self):
        return '{}-sem-{}'.format(self.academics.student.name, self.academics.semester)


class InternalExam(models.Model):
    name = models.CharField(max_length=30)
    mark_detail = models.ForeignKey(InternalMarkDetail, related_name="internal_exam")

    def __unicode__(self):
        return '{}'.format(self.name)


class InternalExamSubject(models.Model):
    internal_exam = models.ForeignKey(InternalExam, related_name="internal_exam_subject")
    subject_code = models.CharField(max_length=20)
    subject_name = models.CharField(max_length=50)
    min_mark = models.IntegerField()
    max_mark = models.IntegerField()
    obtained_mark = models.IntegerField()
    first_mark = models.IntegerField()
    status = models.CharField(max_length=5, choices=(("Pass","Pass"), ("Fail", "Fail")))

    def __unicode__(self):
        return '{}'.format(self.subject_code)


class LibraryStatus(models.Model):
    book_name = models.CharField(max_length=64)
    book_id = models.CharField(max_length=32)
    issued_date = models.DateField(default=datetime.date.today)
    renewal_date = models.DateField(default=datetime.date.today)
    return_date = models.DateField(default=datetime.date.today)
    fine_amt = models.FloatField()
    status = models.CharField(max_length=10,choices=(('ISSUED','ISSUED'),('RENEWED','RENEWED'),('RETURNED','RETURNED')))
    student = models.ForeignKey(Student, related_name="library_status")

    def __unicode__(self):
        return '{}'.format(self.book_name)

