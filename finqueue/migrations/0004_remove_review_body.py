# Generated by Django 3.0.8 on 2020-08-07 04:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('finqueue', '0003_auto_20200807_0420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='body',
        ),
    ]
