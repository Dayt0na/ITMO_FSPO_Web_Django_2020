# Generated by Django 3.1.2 on 2020-10-13 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('final_lab', '0004_auto_20201013_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='Table_number',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='Табличный номер'),
        ),
    ]
