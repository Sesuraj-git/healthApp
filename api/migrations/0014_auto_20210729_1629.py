# Generated by Django 3.2.5 on 2021-07-29 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_doctor_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
