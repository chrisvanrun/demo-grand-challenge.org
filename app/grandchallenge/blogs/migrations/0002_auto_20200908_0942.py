# Generated by Django 3.0.9 on 2020-09-08 09:42

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("blogs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="authors",
            field=models.ManyToManyField(
                related_name="blog_authors", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
