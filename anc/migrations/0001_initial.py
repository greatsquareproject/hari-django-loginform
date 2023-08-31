# Generated by Django 4.2.4 on 2023-08-28 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField(max_length=10)),
                ('name', models.CharField(max_length=30)),
                ('s_year', models.IntegerField(max_length=4)),
                ('s_section', models.CharField(max_length=1)),
                ('s_depart', models.CharField(max_length=30)),
            ],
        ),
    ]
