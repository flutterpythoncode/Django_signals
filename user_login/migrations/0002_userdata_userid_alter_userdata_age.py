# Generated by Django 5.1 on 2025-03-11 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_login', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdata',
            name='userid',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='userdata',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
