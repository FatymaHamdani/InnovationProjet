# Generated by Django 2.2.7 on 2019-12-03 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0016_auto_20191203_1717'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='state_comment',
            field=models.CharField(blank=True, help_text='Make your title attention-grabbing and informative.', max_length=255, null=True, verbose_name='Title comment '),
        ),
    ]
