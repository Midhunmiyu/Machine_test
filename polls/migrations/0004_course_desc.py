# Generated by Django 4.2.3 on 2023-07-04 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
