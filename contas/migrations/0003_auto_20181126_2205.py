# Generated by Django 2.1.3 on 2018-11-26 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0002_auto_20181126_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transacao',
            name='data',
            field=models.DateTimeField(),
        ),
    ]