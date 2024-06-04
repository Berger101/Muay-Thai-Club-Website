from django.conf import settings


def google_maps_api_key(request):
    return {
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }


def emailjs_settings(request):
    return {
        'EMAILJS_SERVICE_ID': settings.EMAILJS_SERVICE_ID,
        'EMAILJS_TEMPLATE_ID': settings.EMAILJS_TEMPLATE_ID,
        'EMAILJS_PUBLIC_KEY': settings.EMAILJS_PUBLIC_KEY,
    }
