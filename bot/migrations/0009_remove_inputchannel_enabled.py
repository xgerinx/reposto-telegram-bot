# Generated by Django 4.1.1 on 2022-10-12 20:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0008_alter_inputchannel_enabled'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inputchannel',
            name='enabled',
        ),
    ]
