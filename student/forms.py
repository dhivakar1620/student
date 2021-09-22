from django import forms
from .models import Students,Marks

class Cstudent_dbf(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name','roll_no','dob']


class Cmark_dbf(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['idd','mark']
