# Generated by Django 2.0 on 2017-12-14 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collabstudio', '0003_auto_20171214_1033'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
    ]
