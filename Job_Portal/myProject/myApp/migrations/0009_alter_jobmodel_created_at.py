# Generated by Django 5.0.1 on 2024-10-30 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0008_jobmodel_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobmodel',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]