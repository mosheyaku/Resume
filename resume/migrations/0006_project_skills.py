# Generated by Django 5.2.3 on 2025-06-23 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0005_remove_skill_icon_image_skill_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='skills',
            field=models.ManyToManyField(related_name='projects', to='resume.skill'),
        ),
    ]
