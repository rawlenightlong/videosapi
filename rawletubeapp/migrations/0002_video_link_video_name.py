# Generated by Django 4.1.7 on 2023-02-22 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rawletubeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='link',
            field=models.CharField(default='https://www.youtube.com/watch?v=7PjMN6STgPY&ab_channel=Marty', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='video',
            name='name',
            field=models.CharField(default='video', max_length=100),
            preserve_default=False,
        ),
    ]
