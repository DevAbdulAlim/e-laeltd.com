# Generated by Django 4.2 on 2023-04-26 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_employee_department_employee_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salary',
            name='paid_date',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterUniqueTogether(
            name='salary',
            unique_together={('employee', 'month', 'year')},
        ),
    ]
