# Generated by Django 4.0.1 on 2022-01-28 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_tag_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tagposition',
            name='is_main',
            field=models.BooleanField(default='False'),
        ),
    ]
