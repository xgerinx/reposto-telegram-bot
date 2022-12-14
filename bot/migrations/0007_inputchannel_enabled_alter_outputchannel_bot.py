# Generated by Django 4.1.1 on 2022-10-12 19:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0006_rename_repostchannel_outputchannel'),
    ]

    operations = [
        migrations.AddField(
            model_name='inputchannel',
            name='enabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='outputchannel',
            name='bot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='output_channels', to='bot.bot'),
        ),
    ]
