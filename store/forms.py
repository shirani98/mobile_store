from django import forms

from .models import Mobile


class MobileForm(forms.ModelForm):
    class Meta:
        model = Mobile
        fields = "__all__"

    def clean_brand_name(self):
        brand_name = self.cleaned_data.get("brand_name")
        if len(brand_name) <= 2:
            raise forms.ValidationError("Brand_name is wrong.")
        return brand_name

    def clean_size(self):
        size = self.cleaned_data.get("size")
        if size <= 2:
            raise forms.ValidationError("Size must be a valid number.")
        return size
