# Generated by Django 4.0.4 on 2022-07-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('screener', '0003_alter_company_company_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='slug',
            field=models.SlugField(auto_created=True, blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_name',
            field=models.CharField(max_length=200),
        ),
    ]