# Generated by Django 4.2.7 on 2023-11-22 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0002_alter_task_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('is_completed', 'deadline', 'priority')},
        ),
    ]
