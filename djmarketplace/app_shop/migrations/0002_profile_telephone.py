# Generated by Django 4.0 on 2024-03-14 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='telephone',
            field=models.CharField(default='+7(000)000-00-00', max_length=16),
        ),
    ]
