# Generated by Django 4.1 on 2023-07-04 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("movieapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="movie",
            name="img",
            field=models.ImageField(default="sdsdsds", upload_to="gallery"),
            preserve_default=False,
        ),
    ]
