# Generated by Django 4.0.4 on 2022-07-19 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsvibes', '0009_remove_person_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='password',
            field=models.CharField(default=None, max_length=100),
        ),
    ]