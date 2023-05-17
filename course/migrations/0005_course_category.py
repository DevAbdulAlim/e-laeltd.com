# Generated by Django 4.2 on 2023-04-16 09:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_branch_category_service'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='course.category'),
            preserve_default=False,
        ),
    ]
