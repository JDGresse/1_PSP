from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Name", max_length=100, required=True)
    email = forms.EmailField(label="Email", max_length=100, required=True)
    contact_number = forms.CharField(
        label="Contact number", max_length=15, required=True
    )
    subject = forms.CharField(label="Subject", max_length=100, required=True)
    service_choices = [
        ("Psychotherapy", "Psychotherapy"),
        ("AD/HD Support", "AD/HD Support"),
        ("Neurodiversity", "Neurodiversity"),
        ("Other", "Other"),
    ]
    service = forms.ChoiceField(label="Service", choices=service_choices)
    message = forms.CharField(label="Message", widget=forms.Textarea, required=False)
