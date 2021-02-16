from django import forms
from models.grade import Grade
import io
import csv

class GradeForm(forms.Form):
    data_file = forms.FileField()
    
    def process_data(self):
        f = io.TextIOWrapperself.cleaned_data['data_file'].file
        reader = csv.DictReader(f)
        
        for grade in reader:
            g = Grade(courseCode = grade['code'], matricNo = grade['matricNo'], alphanum = ['alphanum'])
            g.save()