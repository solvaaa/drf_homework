# Generated by Django 4.2.6 on 2023-10-09 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_lesson_course_alter_payment_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='payment',
            options={'verbose_name': 'платёж', 'verbose_name_plural': 'платежи'},
        ),
    ]
