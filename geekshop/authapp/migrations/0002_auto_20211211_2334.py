# Generated by Django 3.1.3 on 2021-12-11 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='age',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='возраст'),
        ),
    ]
