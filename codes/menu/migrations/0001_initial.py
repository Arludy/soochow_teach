# Generated by Django 4.2.3 on 2023-07-12 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='noone', max_length=20)),
                ('salary', models.IntegerField(default=0)),
                ('selfDesc', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=20)),
                ('w_sex', models.CharField(max_length=20)),
                ('age', models.CharField(max_length=20)),
                ('w_edu', models.CharField(max_length=20)),
                ('w_time', models.IntegerField()),
                ('mail', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('grade', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Anonymous', max_length=20)),
                ('salary', models.PositiveIntegerField(default=0)),
                ('selfDesc', models.CharField(default='', max_length=100)),
                ('subjects', models.CharField(max_length=20)),
                ('sex', models.CharField(default='Null', max_length=4)),
                ('edu', models.CharField(default='Null', max_length=20)),
                ('time', models.PositiveIntegerField()),
                ('mail', models.CharField(max_length=30)),
                ('wechart_number', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('experience', models.CharField(max_length=50)),
            ],
        ),
    ]