# Generated by Django 3.2.18 on 2023-04-14 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_profile_content'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='content',
            new_name='bio',
        ),
        migrations.AddField(
            model_name='profile',
            name='name',
            field=models.TextField(blank=True, max_length=4000),
        ),
    ]
