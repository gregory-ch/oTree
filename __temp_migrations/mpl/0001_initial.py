# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2019-07-24 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models
import otree_save_the_change.mixins


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('otree', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_subsession', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_group', to='otree.Session')),
            ],
            options={
                'db_table': 'mpl_group',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_gbat_arrived', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('_gbat_grouped', otree.db.models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=False)),
                ('choice_1', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_2', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_3', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_4', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_5', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_6', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_7', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_8', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_9', otree.db.models.StringField(max_length=10000, null=True)),
                ('choice_10', otree.db.models.StringField(max_length=10000, null=True)),
                ('random_draw', otree.db.models.IntegerField(null=True)),
                ('choice_to_pay', otree.db.models.StringField(max_length=10000, null=True)),
                ('option_to_pay', otree.db.models.StringField(max_length=10000, null=True)),
                ('inconsistent', otree.db.models.IntegerField(null=True)),
                ('switching_row', otree.db.models.IntegerField(null=True)),
                ('av_switching_row', otree.db.models.FloatField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mpl.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mpl_player', to='otree.Session')),
            ],
            options={
                'db_table': 'mpl_player',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='mpl_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'mpl_subsession',
            },
            bases=(otree_save_the_change.mixins.SaveTheChange, models.Model),
        ),
        migrations.AddField(
            model_name='player',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mpl.Subsession'),
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mpl.Subsession'),
        ),
    ]
