# Generated by Django 2.2 on 2023-01-02 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageData', '0003_auto_20230102_0150'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='inClass',
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
