from django import forms
from .models import Salesman
from django.core.exceptions import ValidationError
from django.forms import DateInput, TextInput, ImageField


class SalesmanForm(forms.ModelForm):
    class Meta:
        model = Salesman
        fields = '__all__'
        widgets = { "date_to_work":DateInput(attrs={'type':'date'})}


    def __init__(self, *args , **kwargs):
        super(SalesmanForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']= 'form-control'