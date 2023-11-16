# Generated by Django 4.2.7 on 2023-11-16 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=3, unique=True, verbose_name='Currency')),
                ('exchange_rete_to_usd', models.CharField(max_length=10, verbose_name='Rate')),
            ],
            options={
                'verbose_name': 'Payments',
                'verbose_name_plural': 'Payments',
                'ordering': ['currency'],
            },
        ),
    ]
