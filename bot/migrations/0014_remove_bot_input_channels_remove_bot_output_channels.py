# Generated by Django 4.1.1 on 2022-10-17 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0013_botchannelbinding'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bot',
            name='input_channels',
        ),
        migrations.RemoveField(
            model_name='bot',
            name='output_channels',
        ),
    ]
