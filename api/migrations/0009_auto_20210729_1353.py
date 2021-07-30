# Generated by Django 3.2.5 on 2021-07-29 13:53

import api.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20210729_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.user'),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doc_mobile',
            field=models.CharField(max_length=10, validators=[api.validators.valid_mob]),
        ),
        migrations.DeleteModel(
            name='Patient',
        ),
    ]