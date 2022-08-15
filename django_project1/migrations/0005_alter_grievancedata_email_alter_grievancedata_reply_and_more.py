# Generated by Django 4.1 on 2022-08-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('django_project1', '0004_grievancedata_usermodel_email_usermodel_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grievancedata',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='grievancedata',
            name='reply',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='grievancedata',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
        migrations.AlterField(
            model_name='usermodel',
            name='username',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
