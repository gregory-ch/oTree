# Generated by Django 2.2.12 on 2020-07-28 13:11

from django.db import migrations
import otree.db.models


class Migration(migrations.Migration):

    dependencies = [
        ('roshambo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='randome_move',
            field=otree.db.models.FloatField(null=True),
        ),
    ]