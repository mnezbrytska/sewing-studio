from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from studio.models import Tailor, Order, Service


class TailorCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Tailor
        fields = UserCreationForm.Meta.fields + ("first_name", "last_name", "email" )
        # fields = UserCreationForm.Meta.fields + ("license_number",)


class OrderForm(forms.ModelForm):
    services = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta:
        model = Order
        fields = "__all__"


class TailorSearchForm(forms.Form):
    username = forms.CharField(
        max_length=60,
        # required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Username"}),
    )


class OrderSearchForm(forms.Form):
    short_description = forms.CharField(
        max_length=60,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "description"}),
    )


class ServiceSearchForm(forms.Form):
    name = forms.CharField(
        max_length=160,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "name"}),
    )


class CustomerSearchForm(forms.Form):
    last_name = forms.CharField(
        max_length=160,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "last_name"}),
    )
