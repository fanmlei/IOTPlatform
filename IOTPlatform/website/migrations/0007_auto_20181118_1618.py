# Generated by Django 2.1.2 on 2018-11-18 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20181118_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='datastream',
            name='qos',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
