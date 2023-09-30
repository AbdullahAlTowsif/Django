from django import forms
from first_app.models import StudentModel
class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentModel
        fields = '__all__' #-> shows all
        # fields = ['name', 'roll'] -> only shows this two
        # exclude = ['roll'] -> shows all except roll
        labels = {
            'name': 'Student Name',
            'roll': 'Student Roll'
        }
        widgets = {
            'name' : forms.TextInput(attrs={'class' : 'btn-primary'}),
            # 'roll' : forms.PasswordInput()
        }
        help_texts = {
            'name' : "Write your full name"
        }