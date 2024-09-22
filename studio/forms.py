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




    # def clean_license_number(self):
    #     license_num = self.cleaned_data["license_number"]
    #     if not license_num[:3].isupper() or not license_num[:3].isalpha():
    #         raise ValidationError(
    #             "First 3 characters must be uppercase letters."
    #         )
    #
    #     if not license_num[3:].isdigit():
    #         raise ValidationError("Last 5 characters must be digits.")
    #
    #     return license_num