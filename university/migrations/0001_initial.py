# Generated by Django 4.0.3 on 2022-04-08 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField(default=0)),
                ('marital_status', models.CharField(choices=[('single', 'single'), ('married', 'married')], max_length=10)),
                ('height', models.IntegerField(default=1)),
                ('gsp_location', models.CharField(max_length=20)),
                ('cam_photo', models.FileField(upload_to='images')),
                ('iq_test', models.IntegerField(default=0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['date_created'],
            },
        ),
    ]
