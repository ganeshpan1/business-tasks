# Generated by Django 4.2.7 on 2023-11-06 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('owner_info', models.CharField(max_length=100)),
                ('employee_size', models.IntegerField()),
            ],
        ),
    ]
