from django import forms

from .models import item

INPUT_class = 'w-full py-4 px-6 rounded-xl border-2 border-solid'

class NewItemform(forms.ModelForm):
    class Meta:
        model= item
        fields = ("category","name","description","price","image")
        widgets = {
                'category': forms.Select(attrs={
                    'class': INPUT_class
                }),

                'name': forms.TextInput(attrs={
                    'class': INPUT_class
                }),

                'description': forms.Textarea(attrs={
                    'class': INPUT_class
                }),

                'price': forms.TextInput(attrs={
                    'class': INPUT_class
                }),

                'image': forms.FileInput(attrs={
                    'class': INPUT_class
                })
        }

class EditItemform(forms.ModelForm):
    class Meta:
        model= item
        fields = ("name","description","price","image", "is_sold")
        widgets = {

                'name': forms.TextInput(attrs={
                    'class': INPUT_class
                }),

                'description': forms.Textarea(attrs={
                    'class': INPUT_class
                }),

                'price': forms.TextInput(attrs={
                    'class': INPUT_class
                }),

                'image': forms.FileInput(attrs={
                    'class': INPUT_class
                })
        }