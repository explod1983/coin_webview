# Generated by Django 3.2.3 on 2021-05-15 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('morda', '0004_alter_coin_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
