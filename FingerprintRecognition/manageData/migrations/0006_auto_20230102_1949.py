# Generated by Django 2.2 on 2023-01-02 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manageData', '0005_auto_20230102_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='finger_image',
            field=models.ImageField(null=True, upload_to='data/<django.db.models.fields.CharField>'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='sample',
            field=models.IntegerField(default=0, editable=False, verbose_name='Number of Sample'),
        ),
    ]