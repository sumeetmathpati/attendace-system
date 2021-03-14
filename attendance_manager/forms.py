from django.forms import ModelChoiceField, EmailField, Form
from .models import Class


# class TakeAttendance(forms.Form):
#     email = forms.EmailField()

#     class Meta():
#         model = Class
#         fields = ['title']


class TakeAttendance(Form):

    # email = EmailField(readonly = True).attrs['readonly']
    class_name = ModelChoiceField(queryset=Class.objects.all(), to_field_name="title")
    
