# Generated by Django 4.1 on 2023-07-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todoapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="task",
            name="date",
            field=models.DateField(default="1994-02-21"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="task",
            name="name",
            field=models.TextField(max_length=250),
        ),
    ]
