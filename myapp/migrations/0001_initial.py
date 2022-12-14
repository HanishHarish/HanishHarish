# Generated by Django 3.2.7 on 2021-11-08 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('mobile', models.CharField(max_length=12, verbose_name='mobile')),
                ('address', models.CharField(max_length=100, verbose_name='address')),
                ('email', models.CharField(max_length=30, verbose_name='email')),
                ('designation', models.CharField(max_length=20, verbose_name='designation')),
            ],
        ),
    ]
