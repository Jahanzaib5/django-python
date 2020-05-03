# Generated by Django 2.0.7 on 2020-05-03 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Flights', '0006_auto_20200503_1808'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_taken',
            name='taken',
        ),
        migrations.AddField(
            model_name='course_taken',
            name='taken',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Taken', to='Flights.Course'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='course_taken',
            name='user',
        ),
        migrations.AddField(
            model_name='course_taken',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='User', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
