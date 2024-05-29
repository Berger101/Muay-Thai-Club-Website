from django.db import migrations


def create_initial_categories(apps, schema_editor):
    Category = apps.get_model('activities', 'Category')
    categories = [
        Category(name='Boxing'),
        Category(name='Thai Boxing'),
        Category(name='BJJ'),
        Category(name='Private Training'),
        Category(name='Group Training'),
        Category(name='Events'),
        Category(name='Corporate Events'),
        Category(name='Children Classes')
    ]
    Category.objects.bulk_create(categories)


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_initial_categories),
    ]
