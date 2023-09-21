from django import forms
from bookings.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['table', 'date', 'time', 'num_guests','notes']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['table'].queryset = Table.objects.filter(availability=True)

    def clean(self):
        cleaned_data=super().clean()