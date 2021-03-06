# Generated by Django 3.1.5 on 2021-01-17 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0007_auto_20210117_1639'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('website', models.URLField()),
                ('cv', models.FileField(upload_to='apply/')),
                ('cover_letter', models.TextField(max_length=500)),
            ],
        ),
    ]
