# Generated by Django 2.2.3 on 2022-01-21 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='customer_id',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
