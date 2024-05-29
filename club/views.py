from django.shortcuts import render


def home(request):
    activities = [
        {
            'title': 'Thai Boxing',
            'image': 'images/muaythai.jpg',
            'link': '/activities/category/thai-boxing/',
        },
        {
            'title': 'Boxing',
            'image': 'images/muay_thai.jpg',
            'link': '/activities/category/boxing/',
        },
        {
            'title': 'BJJ',
            'image': 'images/bjj.jpg',
            'link': '/activities/category/BJJ/',
        },
        {
            'title': 'Private Training',
            'image': 'images/private_training.jpg',
            'link': '/activities/category/private-training/',
        },
        {
            'title': 'Group Training',
            'image': 'images/group_training.jpg',
            'link': '/activities/category/group-training',
        },
        {
            'title': 'Corporate Events',
            'image': 'images/corporate_events.jpg',
            'link': '/activities/category/corporate-events',
        },
        {
            'title': 'Kids Classes',
            'image': 'images/hen_stag_parties.jpg',
            'link': '/activities/category/kids-classes/',
        },
        {
            'title': 'Events',
            'image': 'images/special_events.jpg',
            'link': '/activities/category/events/',
        },
    ]
    return render(request, 'club/home.html', {'activities': activities})
