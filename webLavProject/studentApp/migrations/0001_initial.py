# Generated by Django 3.2.5 on 2023-01-09 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('program_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.SmallIntegerField()),
                ('student_name', models.CharField(max_length=30)),
                ('district', models.CharField(max_length=20)),
                ('cell_no', models.CharField(max_length=11)),
                ('email', models.EmailField(max_length=254)),
                ('doB', models.DateTimeField()),
                ('program_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studentApp.program')),
            ],
        ),
    ]
