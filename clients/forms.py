from django import forms
from .models import Client
from django.core.exceptions import ValidationError

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'

    def __init__(self, *args , **kwargs):
        super(ClientForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']= 'form-control'

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')

        if Client.objects.filter(phone=phone).exists():
            raise ValidationError('Такой номер телефона уже есть!')
        return phone