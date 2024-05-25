# Generated by Django 5.0.4 on 2024-05-24 19:25

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='subCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.SlugField(default=None)),
                ('image', models.ImageField(upload_to='products/')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productApp.category')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productApp.company')),
                ('subCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productApp.subcategory')),
            ],
        ),
    ]
