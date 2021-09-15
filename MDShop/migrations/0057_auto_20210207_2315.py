# Generated by Django 3.1.4 on 2021-02-07 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MDShop', '0056_auto_20210203_0235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customerlike',
            name='like',
        ),
        migrations.AddField(
            model_name='customerlike',
            name='likeNEW',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='MDShop.smartphone'),
        ),
    ]
