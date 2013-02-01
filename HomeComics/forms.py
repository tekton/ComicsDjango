from django import forms
from models import *


class NewSeriesFromData(forms.Form):
    #name = forms.CharField()
    series = forms.CharField()
    max_issue = forms.CharField(required=False)
    min_issue = forms.CharField(required=False)
    orig_id = forms.CharField(widget=forms.HiddenInput)
"""
class NewSeriesFromData(forms.Form):
    series_name = forms.CharField(max_length=255)
    min_issue = forms.CharField(max_length=255)
    max_issue = forms.CharField(max_length=255)
    from_file_id = forms.CharField(max_length=255)
    #### optional inputs
    publisher = forms.CharFiled(max_length=255,required=False)
"""


class SearchFormClass(forms.Form):
    search_data = forms.CharField()
