# Generated by Django 4.1.1 on 2022-10-17 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0018_rename_output_channels_botchannelbinding_output_channel'),
    ]

    operations = [
        migrations.AddField(
            model_name='botchannelbinding',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
    ]
