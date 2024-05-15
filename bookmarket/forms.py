from django.forms import ModelForm
from django import forms
from .models import Review
from .models import Books


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'price', 'image']


class AddReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['comment', 'star_given']
