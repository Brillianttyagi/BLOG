# Generated by Django 3.1.7 on 2021-04-11 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('heading', models.CharField(max_length=100)),
                ('body', models.CharField(max_length=100000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('auther', models.CharField(max_length=60)),
                ('read_time', models.IntegerField()),
            ],
        ),
    ]
