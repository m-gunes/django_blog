from django import forms

class RegistrationForm(forms.Form):
   username = forms.CharField(max_length=150, min_length=3, label='username')
   password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='password')
   confirm = forms.CharField(max_length=50, widget=forms.PasswordInput, label='password confirm')

   def clean(self):
      #super().clean()
      username = self.cleaned_data.get('username')
      password = self.cleaned_data.get('password')
      confirm = self.cleaned_data.get('confirm')

      if password and confirm and password != confirm:
         raise forms.ValidationError('parolalar eslesmiyor')

      values = {
         'username': username,
         'password': password
      }
      return values



class LoginForm(forms.Form):
   username = forms.CharField(label='User Name', widget=forms.TextInput(attrs={'class': 'custom-class'}))
   password = forms.CharField(label='Password', widget=forms.PasswordInput)