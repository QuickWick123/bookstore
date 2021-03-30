from django import forms
from bookstore_api.models import UserProfiles


class CreateWishForm(forms.ModelForm):

    class Meta:
        model = UserProfiles
        fields = ('wishlistName',)
