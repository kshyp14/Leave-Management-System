# Generated by Django 2.0.3 on 2018-03-14 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='prefix',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='suffix',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='application',
            name='typeOfLeave',
            field=models.CharField(choices=[('EL', 'Earned Leave'), ('HPL', 'Half Pay Leave'), ('OT', 'Other Leave')], default='OT', max_length=3),
            preserve_default=False,
        ),
    ]