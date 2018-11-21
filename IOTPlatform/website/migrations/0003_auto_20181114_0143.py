# Generated by Django 2.1.2 on 2018-11-14 01:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20181110_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='apiKey',
            field=models.CharField(max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='device',
            name='dev_introduce',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='device',
            name='tag',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
