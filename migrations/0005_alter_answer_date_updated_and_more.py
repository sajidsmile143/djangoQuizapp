# Generated by Django 4.1.1 on 2022-09-21 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_alter_answer_date_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last_Updated'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='date_updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Last_Updated'),
        ),
    ]