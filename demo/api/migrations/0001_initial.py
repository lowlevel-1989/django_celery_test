# Generated by Django 2.2.4 on 2019-08-27 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.UUIDField(editable=False, primary_key=True, serialize=False)),
                ('task_id', models.CharField(max_length=255)),
                ('output', models.IntegerField(null=True)),
            ],
        ),
    ]