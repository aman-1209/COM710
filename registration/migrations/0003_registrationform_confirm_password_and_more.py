# Generated by Django 5.0.6 on 2024-05-22 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_alter_registrationform_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='registrationform',
            name='confirm_password',
            field=models.CharField(blank=True, max_length=128),
        ),
        migrations.AlterField(
            model_name='registrationform',
            name='mobile_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
