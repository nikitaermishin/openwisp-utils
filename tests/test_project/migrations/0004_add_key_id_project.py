# Generated by Django 2.0.13 on 2019-04-21 19:50

import django.core.validators
from django.db import migrations, models
import openwisp_utils.utils
import re
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('test_project', '0003_project_operator'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='key',
            field=models.CharField(db_index=True, default=openwisp_utils.utils.get_random_key, help_text='unique device key', max_length=64, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[^\\s/\\.]+$'), code='invalid', message='Key must not contain spaces, dots or slashes.')]),
        ),
        migrations.AlterField(
            model_name='project',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]