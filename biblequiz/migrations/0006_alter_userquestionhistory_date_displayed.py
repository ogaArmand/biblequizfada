# Generated by Django 4.1.8 on 2024-03-19 22:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblequiz', '0005_userquestionhistory_is_affiche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userquestionhistory',
            name='date_displayed',
            field=models.DateField(null=True),
        ),
    ]
