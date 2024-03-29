# Generated by Django 2.1.7 on 2019-04-06 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20190405_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='extra_cheese',
        ),
        migrations.AlterField(
            model_name='order',
            name='dinner_platters',
            field=models.ManyToManyField(blank=True, related_name='order', to='orders.DinnerPlatter'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pastas',
            field=models.ManyToManyField(blank=True, related_name='order', to='orders.Pasta'),
        ),
        migrations.AlterField(
            model_name='order',
            name='pizzas',
            field=models.ManyToManyField(blank=True, related_name='order', to='orders.Pizza'),
        ),
        migrations.AlterField(
            model_name='order',
            name='salads',
            field=models.ManyToManyField(blank=True, related_name='order', to='orders.Salad'),
        ),
        migrations.AlterField(
            model_name='order',
            name='subs',
            field=models.ManyToManyField(blank=True, related_name='order', to='orders.Sub'),
        ),
    ]
