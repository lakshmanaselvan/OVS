from django import forms
from django.forms import ModelForm
from .models import Voter

class VoterForm(ModelForm):
    class Meta:
        model = Voter
        fields = ('voter_id','voter_name','password','email')

        labels = {
            'voter_id':'',
            'voter_name':'',
            'password':'',
            'email':'',
        }

        widgets = {
            'voter_id':forms.TextInput(attrs={'class':'form-control','placeholder':'Voter ID'}),
            'voter_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Voter Name'}),
            'password':forms.TextInput(attrs={'class':'form-control','placeholder':'Password'}),
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':'Email'}),
        }