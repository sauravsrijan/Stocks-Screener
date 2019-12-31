# Generated by Django 3.0.1 on 2019-12-31 09:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('market', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='creator',
            field=models.ForeignKey(blank=True, db_column='Creator', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='stock_creator', to=settings.AUTH_USER_MODEL),
        ),
    ]