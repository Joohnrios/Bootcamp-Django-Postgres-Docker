# Generated by Django 4.1.5 on 2023-01-19 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, null=True)),
                ('event_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'event',
            },
        ),
    ]
