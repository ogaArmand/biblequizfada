# Generated by Django 4.1.8 on 2024-03-21 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblequiz', '0006_alter_userquestionhistory_date_displayed'),
    ]

    operations = [
        migrations.AddField(
            model_name='userresponse',
            name='date_displayed',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]