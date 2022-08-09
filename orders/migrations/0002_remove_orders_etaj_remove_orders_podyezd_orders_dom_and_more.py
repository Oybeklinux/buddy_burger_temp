# Generated by Django 4.0.3 on 2022-08-07 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='etaj',
        ),
        migrations.RemoveField(
            model_name='orders',
            name='podyezd',
        ),
        migrations.AddField(
            model_name='orders',
            name='dom',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='orders',
            name='kvartal',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='orders',
            name='delivery',
            field=models.CharField(choices=[('dostavka', 'Доставка'), ('samovizov', 'Самовывоз')], max_length=20),
        ),
        migrations.AlterField(
            model_name='orders',
            name='kvartira',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]