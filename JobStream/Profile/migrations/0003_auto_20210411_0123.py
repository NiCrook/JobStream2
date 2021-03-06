# Generated by Django 3.1.7 on 2021-04-11 06:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Profile', '0002_auto_20210409_2153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidateprofile',
            name='id',
        ),
        migrations.RemoveField(
            model_name='companyprofile',
            name='id',
        ),
        migrations.AlterField(
            model_name='candidateprofile',
            name='candidate_username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='companyprofile',
            name='company_username',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
