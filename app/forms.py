from django import forms
from app.models import Todo

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']  # Only include fields that exist in your model