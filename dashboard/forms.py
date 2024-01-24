from django import forms
from items.models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border' 

class EditItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=('name','description','price','image','is_sold',)

        widgets={
            'name':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'description':forms.TextInput(attrs={
                'class':INPUT_CLASSES
            }),
            'price':forms.NumberInput(attrs={
                'class':INPUT_CLASSES
            }),
            'image':forms.FileInput(attrs={
                'class':INPUT_CLASSES
            }),

        }