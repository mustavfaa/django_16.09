# Generated by Django 3.1.4 on 2021-01-21 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0033_auto_20210122_0156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='like',
            options={},
        ),
        migrations.AlterField(
            model_name='customer',
            name='likecus',
            field=models.ManyToManyField(blank=True, null=True, to='MDShop.smartphone', verbose_name='лайк'),
        ),
    ]