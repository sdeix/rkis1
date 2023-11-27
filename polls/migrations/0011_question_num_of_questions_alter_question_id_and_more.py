# Generated by Django 4.2.7 on 2023-11-27 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0010_alter_question_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='num_of_questions',
            field=models.IntegerField(default=3),
        ),
        migrations.AlterField(
            model_name='question',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 11, 27, 21, 10, 15, 592150), verbose_name='date published'),
        ),
    ]
