# Generated by Django 3.2.5 on 2021-07-29 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0021_alter_appointment_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.doctor'),
        ),
    ]
