from django import forms
from .models import Products
from django.core.exceptions import ValidationError


class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'

    def __init__(self, *args , **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class']= 'form-control'

    def clean_cost(self):
        datacost = self.cleaned_data['cost']
        if datacost < 0:
            raise ValidationError('Некорректная цена')
        return datacost

    def clean_count(self):
        datacount = self.cleaned_data['count']
        if datacount < 0:
            raise ValidationError('Некорректная количество')
        return datacount
