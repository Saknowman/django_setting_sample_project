# Generated by Django 2.2.7 on 2019-11-11 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.IntegerField(choices=[(1, 'TODO'), (2, 'DOING'), (3, 'DONE'), (4, 'NEW_STATUS')]),
        ),
    ]