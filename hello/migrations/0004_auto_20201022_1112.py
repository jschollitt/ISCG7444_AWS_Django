# Generated by Django 3.1.2 on 2020-10-21 22:12

from django.db import migrations, models
import django.utils.timezone
import gettingstarted.storage_backends


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0003_auto_20200826_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='StoreFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=120)),
                ('file', models.FileField(storage=gettingstarted.storage_backends.PrivateMediaStorage(), upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='due_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
