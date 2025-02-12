# Generated by Django 5.1.5 on 2025-02-06 11:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userdetails', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bankdetails',
            name='basic_info',
        ),
        migrations.RemoveField(
            model_name='educationdetails',
            name='basic_info',
        ),
        migrations.RemoveField(
            model_name='previouswork',
            name='basic_info',
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userdetails.bankdetails')),
                ('basic_info', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userdetails.basicinformation')),
                ('education_details', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userdetails.educationdetails')),
                ('previous_work', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='userdetails.previouswork')),
            ],
        ),
    ]
