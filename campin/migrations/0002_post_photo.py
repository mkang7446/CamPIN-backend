# Generated by Django 4.0.3 on 2022-04-09 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(blank=True, default='images/default.jpg', upload_to='images/'),
        ),
    ]
