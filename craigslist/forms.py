from django import forms
from .models import Listing
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm

from .models import Profile
from .models import Post


CONDITIONS = (
    ('NEW', 'New'),
    ('OPEN_BOX', 'Open Box'),
    ('USED', 'Used'),
    ('REFURBISHED', 'Refurbished'),
    ('FOR_PARTS', 'For Parts or Not Working'),
)

CATEGORIES = (
    ('FURNITURE', 'Furniture'),
    ('TEXTBOOKS', 'Textbooks'),
    ('HOUSING', 'Housing'),
    ('SERVICES', 'Services'),
    ('GIGS', 'Gigs'),
    ('LOST_AND_FOUND', 'Lost & Found'),
    ('OTHER', 'Other'),
)

LOCATIONS = (
    ('ALDERMAN LIBRARY', 'Alderman Library'),
    ('CLARK LIBRARY', 'Clark Library'),
    ('CLEMONS LIBRARY', 'Clemons Library'),
    ('THORNTON HALL', 'Thornton Hall'),
    ('CURRY SCHOOL', 'Curry School'),
    ('OTHER', 'Other'),
)

class ListingForm(forms.ModelForm):

    acct = forms.CharField(required=True, initial="default", widget=forms.HiddenInput())
    listing_id = forms.DecimalField(required=True, initial="default", widget=forms.HiddenInput())
    title = forms.CharField(required=True, widget=forms.TextInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'What are you selling?',
            'style': 'width:50ch'
        }
    ))

    price = forms.DecimalField(required=True, widget=forms.NumberInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'How much do you want?',
            'style': 'width:25ch'
        }
    ))

    category = forms.ChoiceField(choices=CATEGORIES, required=True, widget=forms.Select(
        attrs={
            'class' : 'bootstrap-select',
        }
    ))

    location = forms.ChoiceField(choices=LOCATIONS, required=True, widget=forms.Select(
        attrs={
            'class' : 'bootstrap-select',
        }
    ))
    

    condition = forms.ChoiceField(choices=CONDITIONS, required=True, widget=forms.Select(
        attrs={
            'class' : 'bootstrap-select', #rounded_list
        }
    ))

    description = forms.CharField(required=True, widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            'placeholder': 'Provide details about the item.',
            'style': 'width:50ch'
        }
    ))

    images = forms.ImageField(required=True)

    class Meta:

        model = Listing

        fields = ['title', 'price', 'description', 'images', 'category', 'location', 'condition', 'acct', 'listing_id']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'email',
        )

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'birth_date')


class PostForm(ModelForm):
    title = forms.CharField()
    description = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Post
        fields = ('title', 'description',)

