# Generated by Django 2.0.13 on 2019-04-13 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='text',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]
