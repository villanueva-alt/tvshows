from django import forms

class ShowForm(forms.Form):
    title = forms.CharField(max_length=50)
    genre = forms.CharField(max_length=10)
    description = forms.CharField(widget=forms.Textarea(attrs={"Placeholder": "Once upon a time..."}))
    year_released = forms.IntegerField(min_value=1928)