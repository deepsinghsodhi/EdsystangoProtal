# Generated by Django 3.0.7 on 2020-06-13 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_name', models.CharField(max_length=30)),
                ('test_address', models.CharField(max_length=30)),
                ('test_post', models.CharField(max_length=30)),
                ('test_dept', models.CharField(max_length=30)),
            ],
        ),
    ]
