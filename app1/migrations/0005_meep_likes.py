# Generated by Django 4.2.6 on 2023-11-01 16:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0004_profile_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='meep',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='meep_like', to=settings.AUTH_USER_MODEL),
        ),
    ]
