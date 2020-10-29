# Generated by Django 2.2 on 2020-10-09 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0012_auto_20200908_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='DB_apis_log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=10, null=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('api_method', models.CharField(max_length=10, null=True)),
                ('api_url', models.CharField(max_length=1000, null=True)),
                ('api_header', models.CharField(max_length=1000, null=True)),
                ('api_login', models.CharField(max_length=10, null=True)),
                ('api_host', models.CharField(max_length=100, null=True)),
                ('des', models.CharField(max_length=100, null=True)),
                ('body_method', models.CharField(max_length=20, null=True)),
                ('api_body', models.CharField(max_length=1000, null=True)),
                ('sign', models.CharField(max_length=10, null=True)),
                ('file_key', models.CharField(max_length=50, null=True)),
                ('file_name', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
