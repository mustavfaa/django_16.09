# Generated by Django 3.1.4 on 2021-01-02 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0018_auto_20210102_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='likecus',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.CASCADE, to='MDShop.like'),
        ),
    ]