# Generated by Django 3.2.6 on 2021-08-27 18:49

import base.models
import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_company_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, storage=django.core.files.storage.FileSystemStorage(base_url='companies/', location='C:\\Users\\Nitin\\Desktop\\Sem 5\\MPR\\placeme\\src\\placeme\\media/companies/'), upload_to=base.models.image_directory_path),
        ),
    ]
