from django import forms
from .models import *


COLOR_CHOICES =( 
    ("1", "red"), 
    ("2", "blue"), 
    
) 

class CarsForm(forms.ModelForm):
	name = forms.CharField(label='Name', max_length=128)
	color =  forms.ChoiceField(choices= COLOR_CHOICES, label="Color")

	class Meta:
		model = Cars
		fields = '__all__'

class FilterForm(forms.ModelForm):
    
    color =  forms.ChoiceField(choices= COLOR_CHOICES, label="Color")

    class Meta:
        model = Cars
        fields = ['color']
