from django import forms


class UploadFileForm(forms.Form):
    name = forms.CharField(max_length=64)
    file = forms.FileField()
