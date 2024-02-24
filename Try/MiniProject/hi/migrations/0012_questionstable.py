# Generated by Django 5.0 on 2024-02-22 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hi', '0011_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionsTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('QId', models.CharField(max_length=5, unique=True)),
                ('Questions', models.CharField(max_length=100)),
                ('Option1', models.CharField(max_length=100)),
                ('Option2', models.CharField(max_length=100)),
                ('Option3', models.CharField(max_length=100)),
                ('Option4', models.CharField(max_length=100)),
            ],
        ),
    ]