# Generated by Django 2.0 on 2018-05-10 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pastebin', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paste',
            name='number',
        ),
        migrations.RemoveField(
            model_name='paste',
            name='paste_text',
        ),
    ]
