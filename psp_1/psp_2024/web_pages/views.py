from django.shortcuts import render
from django.core.mail import send_mail

from .forms import ContactForm


def home(request):
    return render(request, "web_pages/home.html")


def about(request):
    return render(request, "web_pages/about.html")


def psychotherapy(request):
    return render(request, "web_pages/psychotherapy.html")


def adhd(request):
    return render(request, "web_pages/adhd.html")


def what_to_expect(request):
    return render(request, "web_pages/what_to_expect.html")


def resources(request):
    return render(request, "web_pages/resources.html")


def contact_form(request):

    sent = False

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            clean_form = form.cleaned_data

            send_mail(
                subject=f"PSP Client Inquiry - {clean_form['subject']}",
                message=f"Hi, Penny,\n\nYou have just received the following message from your website contact form:\n\nName: {clean_form['your_name']}\nEmail: {clean_form['email']}\nContact Number: {clean_form['contact_number']}\nService: {clean_form['service']}\nSubject: {clean_form['suject']}\n\nMessage:n{clean_form['message']}",
                from_email=clean_form["email"],
                recipient_list=["jdgresse01@gmail.com"],
            )
            sent = True

    else:
        form = ContactForm()

    return render(
        request,
        "web_pages/contact.html",
        {
            "form": form,
            "sent": sent,
        },
    )
