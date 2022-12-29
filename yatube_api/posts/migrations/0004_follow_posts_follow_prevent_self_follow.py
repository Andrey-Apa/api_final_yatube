# Generated by Django 3.2.16 on 2022-12-29 07:41

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_follow_posts_follow_prevent_self_follow'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='follow',
            constraint=models.CheckConstraint(check=models.Q(('user', django.db.models.expressions.F('following')), _negated=True), name='posts_follow_prevent_self_follow'),
        ),
    ]