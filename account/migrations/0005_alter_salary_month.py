# Generated by Django 4.1.5 on 2023-08-19 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_salary_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='month',
            field=models.IntegerField(choices=[(1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=8),
        ),
    ]
