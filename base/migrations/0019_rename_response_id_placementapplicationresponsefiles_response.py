# Generated by Django 3.2.6 on 2021-09-02 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_auto_20210902_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placementapplicationresponsefiles',
            old_name='response_id',
            new_name='response',
        ),
    ]
