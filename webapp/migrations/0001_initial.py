# Generated by Django 2.2.5 on 2019-09-23 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.IntegerField(primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=32)),
            ],
        ),
    ]
