from django.shortcuts import render


def home(request):
    carousel_items = [
        {
            'image': 'images/muaythai_homeimage.jpg',
            'alt': 'Muay Thai Home Image',
            'heading': 'Welcome to the Muay Thai Club',
            'description': 'This is the home page of the Muay Thai club. Here you can find information about our activities, training sessions, and more.'
        },
        {
            'image': 'images/events.jpg',
            'alt': 'Events',
            'heading': 'Welcome to the Muay Thai Club',
            'description': 'This is the home page of the Muay Thai club. Here you can find information about our activities, training sessions, and more.'
        },
        {
            'image': 'images/kidstraining.jpg',
            'alt': 'Kids Training',
            'heading': 'Welcome to the Muay Thai Club',
            'description': 'This is the home page of the Muay Thai club. Here you can find information about our activities, training sessions, and more.'
        },
    ]

    activities = [
        {
            'title': 'Thai Boxing',
            'image': 'images/muaythai2.jpg',
            'link': '/activities/category/thai-boxing/',
        },
        {
            'title': 'Boxing',
            'image': 'images/boxing.jpg',
            'link': '/activities/category/boxing/',
        },
        {
            'title': 'BJJ',
            'image': 'images/bjj.jpg',
            'link': '/activities/category/BJJ/',
        },
        {
            'title': 'Private Training',
            'image': 'images/privatetraining.jpg',
            'link': '/activities/category/private-training/',
        },
        {
            'title': 'Group Training',
            'image': 'images/grouptraining.jpg',
            'link': '/activities/category/group-training',
        },
        {
            'title': 'Corporate Events',
            'image': 'images/corporateevents.jpg',
            'link': '/activities/category/corporate-events',
        },
        {
            'title': 'Kids Classes',
            'image': 'images/kidstraining.jpg',
            'link': '/activities/category/kids-classes/',
        },
        {
            'title': 'Events',
            'image': 'images/events.jpg',
            'link': '/activities/category/events/',
        },
    ]
    return render(request, 'club/home.html', {'carousel_items': carousel_items, 'activities': activities})
