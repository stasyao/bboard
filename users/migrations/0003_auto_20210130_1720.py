# Generated by Django 3.1.1 on 2021-01-30 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210130_0134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='activation_code',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'пользователь'), ('moderator', 'модератор'), ('admin', 'администратор')], default='user', max_length=20, verbose_name='роль'),
        ),
    ]