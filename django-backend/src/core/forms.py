from django import forms 
from .models import Comments

class Comment(forms.ModelForm):
    class Meta:
        model = Comments
        fields = [
            'body',
            'grade',
        ]