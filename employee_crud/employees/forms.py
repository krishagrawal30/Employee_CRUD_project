from django import forms
from .models import Employee
class Employeeform(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Employeeform, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = True