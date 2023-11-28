# Generated by Django 4.1 on 2023-07-07 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('groups', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('code', models.CharField(default='', max_length=50, unique=True)),
                ('description', models.CharField(blank=True, max_length=100)),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Group', to='groups.group')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('question', models.CharField(max_length=300)),
                ('id', models.IntegerField(default=1, primary_key=True, serialize=False)),
                ('a', models.CharField(max_length=150, null=True)),
                ('b', models.CharField(max_length=150, null=True)),
                ('c', models.CharField(max_length=150, null=True)),
                ('d', models.CharField(max_length=150, null=True)),
                ('answer', models.CharField(default='a', max_length=1, null=True)),
                ('exam', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='questions', to='exams.exam')),
            ],
        ),
    ]