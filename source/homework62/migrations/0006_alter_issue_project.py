# Generated by Django 4.1.7 on 2023-03-15 17:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homework62', '0005_issue_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='homework62.project'),
        ),
    ]
