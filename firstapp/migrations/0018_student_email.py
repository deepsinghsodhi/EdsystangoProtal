# Generated by Django 3.0.7 on 2020-08-06 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0017_feesubmission'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
