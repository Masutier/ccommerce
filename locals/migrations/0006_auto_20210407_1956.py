# Generated by Django 3.1.7 on 2021-04-08 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locals', '0005_auto_20210407_1858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]