# Generated by Django 3.1.6 on 2021-05-31 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20210509_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='devicemanagement',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
