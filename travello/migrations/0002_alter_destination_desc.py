# Generated by Django 5.1.5 on 2025-01-28 09:59

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='destination',
            name='desc',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
