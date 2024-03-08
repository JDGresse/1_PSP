from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label="Name",
        max_length=100,
    )
    email = forms.EmailField(label="Email", max_length=100)
    contact_number = forms.CharField(label="Contact Number", max_length=20)
    service = forms.ChoiceField(
        label="Service",
        choices=(
            ("Psychotherapy", "Psychotherapy"),
            ("AD/HD Support", "AD/HD Support"),
            ("Burnout Coaching", "Burnout Coaching"),
        ),
    )
    subject = forms.CharField(label="Subject", max_length=200)
    message = forms.CharField(label="Message", widget=forms.Textarea)
