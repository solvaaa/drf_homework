# Generated by Django 4.2.6 on 2023-10-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0009_subscription'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='price',
            field=models.FloatField(blank=True, null=True, verbose_name='стоимость'),
        ),
    ]