from django import forms
from .models import UserInfo1, Booking

class UserInfoForm1(forms.ModelForm):
    confirm_password = forms.CharField(label='Confirm Password', max_length=128, widget=forms.PasswordInput)
    class Meta:
        model = UserInfo1
        fields = ['name', 'mail', 'address', 'phoneno','password']
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match. Please enter them again.")

        return cleaned_data

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['user_name', 'event', 'booking_time', 'status']