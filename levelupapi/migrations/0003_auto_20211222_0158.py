# Generated by Django 3.2.9 on 2021-12-22 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('levelupapi', '0002_rename_name_gametype_label'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='desc',
            new_name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='creator',
        ),
        migrations.RemoveField(
            model_name='game',
            name='event',
        ),
        migrations.RemoveField(
            model_name='game',
            name='name',
        ),
        migrations.RemoveField(
            model_name='game',
            name='type',
        ),
        migrations.AddField(
            model_name='event',
            name='date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levelupapi.game', verbose_name='organizer'),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levelupapi.gamer', verbose_name='organizer'),
        ),
        migrations.AddField(
            model_name='game',
            name='game_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='levelupapi.gametype'),
        ),
        migrations.AddField(
            model_name='game',
            name='gamer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='games', to='levelupapi.gamer'),
        ),
        migrations.AddField(
            model_name='game',
            name='maker',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='number_of_players',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='skill_level',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
