# Generated by Django 5.0.7 on 2024-07-19 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0013_course_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('in_review', 'In review'), ('published', 'Published')], default='draft', max_length=25),
        ),
    ]
