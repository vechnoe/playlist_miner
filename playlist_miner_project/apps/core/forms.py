# coding:utf-8

from django import forms
from django.conf import settings

from core.models import Radiostation


class DateFilterForm(forms.Form):
    begin_date = forms.DateField(
        label='Begin',
        input_formats=settings.ACCEPTABLE_FORMATS,
        required=False,
        widget=forms.DateInput(format=settings.DATE_INPUT_FORMAT)
    )

    end_date = forms.DateField(
        label='End',
        required=False,
        input_formats=settings.ACCEPTABLE_FORMATS,
        widget=forms.DateInput(format=settings.DATE_INPUT_FORMAT)
    )

