from django import forms

class GetUserForm(forms.Form):
    user_id = forms.CharField(
        label='User ID',
        widget=forms.TextInput(attrs={'class': 'form-control mb-2'})
    )