# Generated by Django 4.1.1 on 2022-10-17 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0017_alter_botchannelbinding_input_channel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='botchannelbinding',
            old_name='output_channels',
            new_name='output_channel',
        ),
    ]