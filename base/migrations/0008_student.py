# Generated by Django 3.2.6 on 2021-08-28 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0007_company_starting_salary'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('roll_number', models.CharField(max_length=16)),
                ('contact_number', models.CharField(max_length=10)),
                ('college_email_id', models.EmailField(max_length=254)),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('O', 'Other')], max_length=1)),
                ('hometown', models.CharField(max_length=25)),
                ('class10_board', models.CharField(choices=[('ICSE', 'ICSE'), ('SSC', 'SSC'), ('IGCSE', 'IGCSE'), ('CBSE', 'CBSE'), ('IB', 'IB')], max_length=10)),
                ('class10_school', models.CharField(max_length=50)),
                ('class10_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('class12_board', models.CharField(choices=[('HSC', 'HSC'), ('ISC', 'ISC'), ('CBSE', 'CBSE'), ('IB', 'IB'), ('IGCSE', 'IGCSE'), ('Diploma', 'Diploma')], max_length=10)),
                ('class12_college', models.CharField(max_length=50)),
                ('class12_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('undergraduate_stream', models.CharField(choices=[('BE', 'Bachelor of Engineering')], max_length=50)),
                ('undergraduate_specialization', models.CharField(choices=[('Comps', 'Computer Engineering'), ('IT', 'Information Technology'), ('Biomed', 'Biomedical Engineering'), ('EXTC', 'Electronics and Telecommunication'), ('Chemical', 'Chemical Engineering'), ('AI/DS', 'Artificial Intelligence and Data Science'), ('O', 'Other')], max_length=50)),
                ('sem1_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('sem2_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('sem3_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('sem4_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('sem5_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('sem6_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('sem7_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('sem8_sgpi', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4)),
                ('live_kt', models.BooleanField()),
                ('year_drop', models.BooleanField()),
                ('education_gap', models.BooleanField()),
                ('year_joined', models.PositiveSmallIntegerField()),
                ('expected_grad_year', models.PositiveSmallIntegerField()),
                ('resume', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Student',
            },
        ),
    ]
