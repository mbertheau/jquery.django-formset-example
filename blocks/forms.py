from django import forms
from .models import Block

class BlockForm(forms.ModelForm):
    #description = forms.CharField(label='Description', max_length=255)
    class Meta:
    	model = Block
    	fields = '__all__'
