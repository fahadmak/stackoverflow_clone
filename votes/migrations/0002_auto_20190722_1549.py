# Generated by Django 2.2.3 on 2019-07-22 12:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20190722_1502'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('votes', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='QuestionVotes',
            new_name='QuestionVote',
        ),
    ]
