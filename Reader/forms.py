from django import forms


class ReaderForm(forms.Form):
    name = forms.CharField(label="Reader Name", max_length=50)
    lastname = forms.CharField(label="Reader lastname", max_length=70)
    age = forms.IntegerField(label="Reader Age")
    email = forms.EmailField(label="Reader Email")
