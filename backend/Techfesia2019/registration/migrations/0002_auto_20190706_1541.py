# Generated by Django 2.2.2 on 2019-07-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='firebaseuser',
            name='uid',
            field=models.CharField(max_length=150, unique=True),
        ),
    ]
