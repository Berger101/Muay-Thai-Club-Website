from django.shortcuts import render
from .models import Contact


def contact_me(request):
    """
    Renders the Contact page
    """
    contact = Contact.objects.all().order_by('-updated_on').first()

    return render(
        request,
        "contact.html",
        {"contact": contact},
    )
