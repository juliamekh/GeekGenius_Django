# Generated by Django 4.2.11 on 2024-04-15 17:34

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DiabetesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pregnancies', models.FloatField()),
                ('glucose', models.FloatField()),
                ('bloodpressure', models.FloatField()),
                ('skinthickness', models.FloatField()),
                ('insulin', models.FloatField()),
                ('bmi', models.FloatField()),
                ('diabetespedigreefunction', models.FloatField()),
                ('age', models.FloatField()),
                ('probability', models.FloatField()),
            ],
        ),
    ]