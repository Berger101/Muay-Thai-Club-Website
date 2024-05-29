from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.utils.text import slugify


class Category(models.Model):
    BOXING = 'Boxing'
    THAIBOXING = 'Thai Boxing'
    BJJ = 'BJJ'
    PRIVATETRAINING = 'Private Training'
    GROUPTRAINING = 'Group Training'
    EVENTS = 'Events'
    CORPORATEEVENTS = 'Corporate Events'
    KIDSCLASSES = 'Kids Classes'

    CATEGORY_CHOICES = [
        (BOXING, 'Boxing'),
        (THAIBOXING, 'Thai Boxing'),
        (BJJ, 'BJJ'),
        (PRIVATETRAINING, 'Private Training'),
        (GROUPTRAINING, 'Group Training'),
        (EVENTS, 'Events'),
        (CORPORATEEVENTS, 'Corporate Events'),
        (KIDSCLASSES, 'Kids Classes'),
    ]

    name = models.CharField(
        max_length=100, choices=CATEGORY_CHOICES, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class TrainingSession(models.Model):
    title = models.CharField(max_length=200, default='')
    instructor = models.CharField(max_length=100)
    date = models.DateField()
    time = models.TimeField()
    featured_image = CloudinaryField('image', default='placeholder')
    categories = models.ManyToManyField(
        Category, related_name='training_sessions')
    description = models.TextField(default='')
    excerpt = models.TextField(max_length=500, blank=True)

    def __str__(self):
        return f"{self.instructor} - {self.date} {self.time}"
    # def __str__(self):
    #     return self.title


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    session = models.ForeignKey(TrainingSession, on_delete=models.CASCADE)
