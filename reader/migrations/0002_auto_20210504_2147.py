# Generated by Django 3.1.7 on 2021-05-04 16:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reader',
            options={'verbose_name_plural': 'readers'},
        ),
        migrations.AlterField(
            model_name='reader',
            name='phone_number',
            field=models.CharField(blank=True, help_text="Phone number must be entered in the format: '000-555555' or '+999-9999999999'.", max_length=255, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '000-555555' or '+999-9999999999'.", regex='^(0[0-9]{1,2}-[0-9]{6,6})|([0-9]{10})$')]),
        ),
    ]
