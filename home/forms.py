from django import forms
from .models import Team, Location, Contact

class TeamForm(forms.ModelForm):

    class Meta:
        model = Team
        fields = '__all__'

class LocationForm(forms.ModelForm):

    class Meta:
        model = Location
        fields = '__all__'

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'

