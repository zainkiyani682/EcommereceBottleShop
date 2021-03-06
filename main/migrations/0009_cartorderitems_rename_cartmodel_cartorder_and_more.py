# Generated by Django 4.0 on 2022-05-12 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('main', '0008_cartmodel_cartorderitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartOrderItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_no', models.CharField(max_length=150)),
                ('item', models.CharField(max_length=150)),
                ('image', models.CharField(max_length=200)),
                ('qty', models.IntegerField(max_length=200)),
                ('price', models.FloatField()),
                ('total', models.FloatField()),
            ],
        ),
        migrations.RenameModel(
            old_name='CartModel',
            new_name='CartOrder',
        ),
        migrations.DeleteModel(
            name='CartOrderItem',
        ),
        migrations.AddField(
            model_name='cartorderitems',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cartorder'),
        ),
    ]
