# Generated by Django 3.2.5 on 2021-07-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_doctor_has_appointments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='has_appointments',
            field=models.IntegerField(blank=True),
        ),
    ]
