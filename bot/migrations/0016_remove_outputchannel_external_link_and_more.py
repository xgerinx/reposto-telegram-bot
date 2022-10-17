# Generated by Django 4.1.1 on 2022-10-17 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0015_remove_botchannelbinding_output_channel_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='outputchannel',
            name='external_link',
        ),
        migrations.RemoveField(
            model_name='outputchannel',
            name='pin_message_link',
        ),
        migrations.AddField(
            model_name='botchannelbinding',
            name='external_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='botchannelbinding',
            name='pin_message_link',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='promocodereplacement',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='promocode_replacements', to='bot.botchannelbinding'),
        ),
        migrations.AlterField(
            model_name='usernamereplacement',
            name='channel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='username_replacements', to='bot.botchannelbinding'),
        ),
    ]