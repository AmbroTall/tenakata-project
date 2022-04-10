# Generated by Django 4.0.3 on 2022-04-08 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('university', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='registration',
            options={'ordering': ['-date_created']},
        ),
        migrations.AddField(
            model_name='registration',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=10),
            preserve_default=False,
        ),
    ]
