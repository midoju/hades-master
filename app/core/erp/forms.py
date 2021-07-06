from django.forms import ModelForm

from django import forms

from core.erp.models import Category

class CategoryForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for form in self.visible_fields():
            form.field.widget.attrs['class'] = 'form-control'
            form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['name'].widget.attrs['autofocus'] = True
    
    class Meta:
        model = Category
        fields = '__all__'
        labels = {
        }
        widgets = {
            'name': forms.TextInput(
                attrs = {
                    # 'class': 'form-control',
                    'placeholder': 'Ingrese un nombre',
                    #'autocomplete': 'off'
                }
            ),
            'desc': forms.Textarea(
                attrs = {
                    #'class': 'form-control',
                    'placeholder': 'Ingrese una descripción',
                    #'autocomplete': 'off',
                    'rows': 3,
                    'cols': 3,
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data