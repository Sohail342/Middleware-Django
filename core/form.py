from django import forms
import re

class RegForm(forms.Form):
    name = forms.CharField(min_length=5, max_length=20)
    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, min_length=8)
    confirmPassword = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    phone = forms.CharField()
    
    name.widget.attrs.update({"class":"input", "placeholder":"Enter Username"})
    email.widget.attrs.update({"class":"input", "placeholder":"Enter Your Email"})
    password.widget.attrs.update({"class":"input", "placeholder":"Password"})
    confirmPassword.widget.attrs.update({"class":"input", "placeholder":"Confirm Password"})
    phone.widget.attrs.update({"class":"input", "placeholder":"Enter Mobile Number"})
    
    def clean(self):
        clean_data = super().clean()
        password = clean_data.get('password')
        confirmPassword = clean_data.get('confirmPassword')
        phone = clean_data.get('phone')
        errors = []
        
        phone_pattern = re.compile(r'^((\+92 ?)|0)?(3[0-9]{2})[0-9]{7}$')
        if password:
            if password != confirmPassword:
                errors.append('Password not match')
                
            # check numeric and sepeicial characters
            if not any(char.isupper() for char in password):
                errors.append('Password must contain at least one uppercase letter.')
            if not any(char.isdigit() for char in password):
                errors.append('Password must contain at least one numeric character.')
            if not any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/`~' for char in password):
                errors.append('Password must contain at least one special character (eg.!@#$%^&*).')
            if not any(char.islower() for char in password):
                errors.append('Password must contain at least one lowerrcase letter.')
                            
        if phone:    
            if not phone_pattern.match(phone):
                errors.append('Enter a valid Pakistani mobile number (e.g., 03001234567 or +923001234567).')
            
        if errors:
            raise forms.ValidationError(errors)
            
        