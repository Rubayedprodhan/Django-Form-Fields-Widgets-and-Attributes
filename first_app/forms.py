from django import forms
from django.forms.widgets import NumberInput
import datetime
from .models import MyModel


BIRTH_YEAR_CHOICES = ['2000', '2002','2003','2004', '2005']
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]

OPTION_CHOICES = [
        ('logo_design', 'Logo Design'),
        ('domain_selection', 'Domain Selection'),
]


    
class ExampleForm(forms.Form):
    name_first = forms.CharField(label='Your First Name',initial='Your First')
    name_last = forms.CharField(label='Your Last Name',initial='Your Last')
    #comment = forms.CharField(widget=forms.Textarea, label='Your Comment') 
    comment = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField( label='Your Email')
    agree = forms.BooleanField(initial=True)
    date = forms.DateField()
    birth_date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    email_addres = forms.EmailField(
        required=False,
        label="Your Email (Optional)"
    )
    message = forms.CharField(
	max_length = 10,label="This Messa"
    )
    email_address = forms.EmailField( 
    label="Please enter your email address",
    )
    day = forms.DateField(initial=datetime.date.today)
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colo = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colorss = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES,)

    model_choice = forms.ModelChoiceField(
        queryset = MyModel.objects.all(),
        initial = 0
        )
    

    model_choice = forms.ChoiceField(
        choices=OPTION_CHOICES,
        initial='logo_design', 
        label="Model choice*"
    )



    model_choices = forms.MultipleChoiceField(
        choices=OPTION_CHOICES,
        label="Model choices*",
        widget=forms.CheckboxSelectMultiple,  # Renders as checkboxes for multiple selection
    )



   