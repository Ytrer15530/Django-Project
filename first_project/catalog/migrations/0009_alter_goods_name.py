# Generated by Django 4.2.7 on 2023-12-19 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_parametr_goods_parametr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Category name'),
        ),
    ]