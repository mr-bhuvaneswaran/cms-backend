from rest_framework import serializers;

from academics.serializers import AcademicSerializer, LibraryStatusSerializer
from management.serializers import ManagementSerializer
from student.models import Batch, Department, ParentsDetail, MedicalInformation, GeneralInformation, Student, \
    EducationalInformation, FeesDetail, FeesInformation


class FeesDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = FeesDetail
        fields = ('id', 'name', 'apply_date', 'due_date', 'fee_amt')


class FeesInformationSerializer(serializers.ModelSerializer):
    fees_detail = FeesDetailSerializer()

    class Meta:
        model = FeesInformation
        fields = ('id', 'fees_detail', 'paid_fees_amt', 'balance_fees_amt')


class BatchSerializer(serializers.ModelSerializer):
    date_of_join = serializers.DateField(format='%d-%m-%Y')
    year_of_pass = serializers.DateField(format='%Y')

    class Meta:
        model = Batch
        fields = ('id', 'date_of_join', 'year_of_pass')

class DepartmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Department
        fields = ('id', 'name', 'degree')


class ParentsDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = ParentsDetail
        fields = ('id', 'father_name', 'mother_name', 'income')


class MedicalInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = MedicalInformation
        fields = ('id', 'height' , 'weight', 'blood_group', 'physically_challenged',
                  'eye_colour', 'eye_sight', 'mole', 'scar')


class GeneralInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInformation
        fields = ('id', 'gender', 'religion', 'community', 'caste', 'nationality',
                  'mother_tongue', 'place_of_birth', 'financial_category',
                  'admission_type', 'admission_category', 'primary_address', 'secondary_address')


class EducationalInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationalInformation
        fields = ('id', 'course', 'institute', 'place', 'percentage', 'year_of_passedout', )


class StudentSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(format='%d-%m-%Y')
    parent_detail = ParentsDetailSerializer()
    batch = BatchSerializer()
    general_information = GeneralInformationSerializer()
    medical_information = MedicalInformationSerializer()
    fees_information = FeesInformationSerializer(many=True)
    department = DepartmentSerializer()
    educational_informations = EducationalInformationSerializer(many=True)
    management = ManagementSerializer()
    academic = AcademicSerializer(many=True)
    library_status = LibraryStatusSerializer(many=True)
    class Meta:
        model = Student
        fields = ('id', 'name', 'roll_no', 'profile', 'date_of_birth', 'parent_detail',
                  'general_information', 'medical_information', 'fees_information',
                  'batch', 'department', 'academic', 'management', 'educational_informations', 'library_status')