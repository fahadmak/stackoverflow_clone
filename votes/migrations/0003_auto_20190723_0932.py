# Generated by Django 2.2.3 on 2019-07-23 06:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('votes', '0002_auto_20190722_1549'),
    ]

    operations = [
        migrations.RenameField(
            model_name='questionvote',
            old_name='vote_type',
            new_name='vote',
        ),
    ]
