# Generated by Django 3.0.8 on 2020-08-22 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapply', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='image',
            field=models.ImageField(default='download.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='application',
            name='resume',
            field=models.FileField(null=True, upload_to='docs/'),
        ),
    ]