# Generated by Django 5.0.3 on 2024-03-19 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0007_income'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='income',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
