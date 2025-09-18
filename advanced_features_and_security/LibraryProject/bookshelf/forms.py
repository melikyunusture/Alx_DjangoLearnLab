from django import forms

class ExampleForm(forms.Form):
    """
    A simple example form to demonstrate Django's form handling.
    This form includes a text input and a number input field.
    """
    name = forms.CharField(
        max_length=100,
        label='Your Name',
        help_text='Please enter your full name.',
    )
    age = forms.IntegerField(
        label='Your Age',
        help_text='Enter your age as a number.',
    )
