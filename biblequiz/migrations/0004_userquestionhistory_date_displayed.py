# Generated by Django 4.1.8 on 2024-03-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblequiz', '0003_transaction_confirm_transaction_idtransaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='userquestionhistory',
            name='date_displayed',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]