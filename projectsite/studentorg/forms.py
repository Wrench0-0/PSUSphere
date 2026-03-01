from django import forms
from django.forms import ModelForm

from .models import Organization, College, Program, Student, OrgMember


class OrganizationForm(ModelForm):
    class Meta:
        model = Organization
        fields = "__all__"


class CollegeForm(ModelForm):
    class Meta:
        model = College
        fields = "__all__"


class ProgramForm(ModelForm):
    class Meta:
        model = Program
        fields = "__all__"


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"


class OrgMemberForm(ModelForm):
    date_joined = forms.DateField(
        widget=forms.SelectDateWidget(),
    )

    class Meta:
        model = OrgMember
        fields = "__all__"

