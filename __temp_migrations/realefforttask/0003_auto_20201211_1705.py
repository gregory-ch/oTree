# Generated by Django 2.2.12 on 2020-12-11 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realefforttask', '0002_auto_20201211_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='player',
            field=models.ForeignKey(on_delete='', related_name='tasks', to='realefforttask.Player'),
        ),
    ]
