from django import forms

class ContactForm(forms.Form):
    message= forms.CharField(label = "Message", max_length=200)
    email_id=forms.CharField(label="Email Id")
    phone_no=forms.IntegerField(label="Phone No")
        