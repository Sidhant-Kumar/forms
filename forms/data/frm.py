from django import forms

class userform(forms.Form):
    first_name = forms.CharField(label="Enter first  name",max_length=100)

    last_name  = forms.CharField(label="Enter last name", max_length = 100)