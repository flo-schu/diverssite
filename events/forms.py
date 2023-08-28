from django.contrib.auth.models import User
from django.contrib.admin.widgets import AdminDateWidget
from django import forms
from crispy_forms.helper import FormHelper
from django.forms.renderers import BaseRenderer
from crispy_forms.layout import Div, Fieldset, Layout, Row

from .models import PartChoice, Participation, Event

class EventForm(forms.ModelForm):
    part = forms.ModelChoiceField(
        queryset=PartChoice.objects.all(), 
        empty_label=None, required=False, 
        widget=forms.RadioSelect
    )

    class Meta:
        model = Participation
        fields = [
            "id",
            # "part",
            "event",
            "person",
        ]
        widgets = {
            "id": forms.HiddenInput,
            # "part":RadioSelect,
            "event": forms.HiddenInput,
            "person": forms.HiddenInput,
        }



class EditableInputRenderer(BaseRenderer):
    outer_html = '{content}'
    inner_html = '<div editablecontent=true></div>'

class JoinTogaForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["toga"]

class EventTogaForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = [
            "name", "toga", "categ", "location", "date", "end_date", 
            "description", "status",
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'formtextfield'}),
            'date': forms.TextInput(attrs={'class': 'formdetailfield'}),
            'end_date': forms.TextInput(attrs={'class': 'formdetailfield'}),
            "description": forms.Textarea(attrs={"class": "formdetailfield"}),
            # "categ": forms.CheckboxInput(attrs={"class": "badge"})
            # 'toga': forms.TextInput(attrs={'class': 'formtextfield'}),
        }

