# Generated by Django 4.1.3 on 2023-01-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='id',
        ),
        migrations.AlterField(
            model_name='student',
            name='roll_no',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
