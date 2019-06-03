from django import forms
from .models import Scheme

# Define SchemeForm
class SchemeForm(forms.ModelForm):
    class Meta:
        model = Scheme
        fields = ('title', 'description', 'comment', 'completion', 'cost', 'image', 'published_date')