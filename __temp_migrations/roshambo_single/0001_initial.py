# Generated by Django 2.2.12 on 2020-07-28 13:55

from django.db import migrations, models
import django.db.models.deletion
import otree.db.models


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
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roshambo_single_group', to='otree.Session')),
            ],
            options={
                'db_table': 'roshambo_single_group',
            },
        ),
        migrations.CreateModel(
            name='Subsession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('session', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roshambo_single_subsession', to='otree.Session')),
            ],
            options={
                'db_table': 'roshambo_single_subsession',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_in_group', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('_payoff', otree.db.models.CurrencyField(default=0, null=True)),
                ('round_number', otree.db.models.PositiveIntegerField(db_index=True, null=True)),
                ('hum_move', otree.db.models.IntegerField(choices=[[0, 'Камень'], [1, 'Бумага'], [2, 'Ножницы']], null=True)),
                ('comp_move', otree.db.models.IntegerField(null=True)),
                ('result', otree.db.models.IntegerField(null=True)),
                ('randome_move', otree.db.models.FloatField(null=True)),
                ('result_text', otree.db.models.StringField(max_length=10000, null=True)),
                ('comp_move_text', otree.db.models.StringField(max_length=10000, null=True)),
                ('cum_payoff_hum', otree.db.models.FloatField(null=True)),
                ('cum_payoff_comp', otree.db.models.FloatField(null=True)),
                ('cum_payoff_hum_second', otree.db.models.FloatField(null=True)),
                ('cum_payoff_comp_second', otree.db.models.FloatField(null=True)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='roshambo_single.Group')),
                ('participant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roshambo_single_player', to='otree.Participant')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='roshambo_single_player', to='otree.Session')),
                ('subsession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roshambo_single.Subsession')),
            ],
            options={
                'db_table': 'roshambo_single_player',
            },
        ),
        migrations.AddField(
            model_name='group',
            name='subsession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='roshambo_single.Subsession'),
        ),
    ]
