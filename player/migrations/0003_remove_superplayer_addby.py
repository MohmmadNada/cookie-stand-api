# Generated by Django 3.2.5 on 2021-07-25 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0002_alter_superplayer_score'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='superplayer',
            name='addBy',
        ),
    ]
