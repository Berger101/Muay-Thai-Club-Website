from django.shortcuts import render


def home(request):
    activities = [
        {
            'title': 'Thai Boxing',
            'image': 'images/muaythai.jpg',
            'link': '/activities/thai-boxing/',
        },
        {
            'title': 'Classic Boxing',
            'image': 'images/muay_thai.jpg',
            'link': '/activities/classic-boxing/',
        },
        {
            'title': 'BJJ',
            'image': 'images/bjj.jpg',
            'link': '/activities/bjj/',
        },
        {
            'title': 'Private Training',
            'image': 'images/private_training.jpg',
            'link': '/activities/private-training/',
        },
        {
            'title': 'Group Training',
            'image': 'images/group_training.jpg',
            'link': '/activities/group-training/',
        },
        {
            'title': 'Corporate Events',
            'image': 'images/corporate_events.jpg',
            'link': '/activities/corporate-events/',
        },
        {
            'title': 'Child Training',
            'image': 'images/hen_stag_parties.jpg',
            'link': '/activities/hen-stag-parties/',
        },
        {
            'title': 'Events',
            'image': 'images/special_events.jpg',
            'link': '/activities/special-events/',
        },
    ]
    return render(request, 'club/home.html', {'activities': activities})
