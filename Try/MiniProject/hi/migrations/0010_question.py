# Generated by Django 5.0 on 2024-02-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0009_alter_user_managers'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('QId', models.CharField(max_length=5, unique=True)),
                ('Questions', models.CharField(max_length=100)),
                ('Option1', models.CharField(max_length=100)),
                ('Option2', models.CharField(max_length=100)),
                ('Option3', models.CharField(max_length=100)),
                ('Option4', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]