from django import forms
from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label="User Name")
    # file = forms.FileField()
    email = forms.EmailField()
    age = forms.IntegerField()
    weight = forms.FloatField()
    balance = forms.DecimalField()
    birthday = forms.DateField()
    check = forms.BooleanField()
    appoinment = forms.DateTimeField()
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    # MEAL = [('P', 'Pepperoni'),('M','Mashroom',('B','Beef'))]
    # pizza = forms.MultipleChoiceField(choices=MEAL, widget=forms.CheckboxSelectMultiple)

# Module 4.8 Widget =>Do this again
    
# Module 4.9 => Do this again    
# class StudentData(forms.Form):
#     name = forms.CharField(widget=forms.TextInput)
#     email = forms.CharField(widget=forms.EmailInput)
#     def clean_name(self):
#         valname = self.cleaned_data['name']
#         if len(valname) < 10 :
#             raise forms.ValidationError("Enter a name with at least 10 char")
#         return valname


# Module 4.10 => Do this again
# class StudentData(forms.Form):
#     name = forms.CharField(validators=[validators.MaxLengthValidator(10, message='Enter a name with at least 10 characters')])
#     email = forms.CharField(widget=forms.EmailInput)
#     age = forms.CharField()

# Module 4.11 => Do this again
class PasswordValidationProject(forms.Form):
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_conpass = self.cleaned_data['confirm_password']
        if val_conpass != val_pass:
            raise forms.ValidationError("Password doesn't match")