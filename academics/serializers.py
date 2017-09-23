from rest_framework import serializers;

from academics.models import Academic, Attendance, WorkingMonth, ExamResult, SemesterSubject, InternalMarkDetail, \
    InternalExam, InternalExamSubject, LibraryStatus


class WorkingMonthSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingMonth
        fields = ('id', 'month', 'year')


class AttendanceSerializer(serializers.ModelSerializer):
    working_month = WorkingMonthSerializer()

    class Meta:
        model = Attendance
        fields = ('id', 'percentage', 'working_month')


class SemesterSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = SemesterSubject
        fields = ('id', 'sem_no', 'subject_code', 'subject_name', 'grade', 'grade_point', 'credit_point',
                  'status')


class ExamResultSerializer(serializers.ModelSerializer):
    semester_subject = SemesterSubjectSerializer(many=True)

    class Meta:
        model = ExamResult
        fields = ('pk', 'gpa', 'cgpa', 'semester_subject')


class InternalExamSubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternalExamSubject
        fields = ('id', 'subject_code', 'subject_name', 'min_mark', 'max_mark', 'obtained_mark',
                  'first_mark', 'status')


class InternalExamSerializer(serializers.ModelSerializer):
    internal_exam_subject = InternalExamSubjectSerializer(many=True)
    class Meta:
        model = InternalExam
        fields = ('id', 'name', 'internal_exam_subject')


class InternalMarkDetailSerializer(serializers.ModelSerializer):
    internal_exam = InternalExamSerializer(many=True)

    class Meta:
        model = InternalMarkDetail
        fields = ('pk', 'internal_exam')


class AcademicSerializer(serializers.ModelSerializer):
    attendance = AttendanceSerializer(many=True)
    exam_results = ExamResultSerializer()
    internal_mark_detail = InternalMarkDetailSerializer()

    class Meta:
        model = Academic
        fields = ('id', 'semester', 'attendance', 'exam_results', 'internal_mark_detail')


class LibraryStatusSerializer(serializers.ModelSerializer):

    class Meta:
        model = LibraryStatus
        fields = ('id', 'book_name' , 'book_id', 'issued_date', 'renewal_date', 'return_date',
                  'fine_amt', 'status')

