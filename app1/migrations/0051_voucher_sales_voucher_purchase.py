# Generated by Django 4.0.6 on 2022-10-03 10:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0050_remove_stock_itemcreation_company_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='voucher_sales',
            fields=[
                ('no', models.AutoField(primary_key=True, serialize=False)),
                ('Partyname', models.CharField(max_length=255)),
                ('salesledger', models.CharField(max_length=255)),
                ('item', models.CharField(max_length=255)),
                ('rate', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_ledger')),
            ],
        ),
        migrations.CreateModel(
            name='voucher_purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoiceno', models.IntegerField()),
                ('no', models.IntegerField()),
                ('partyname', models.CharField(max_length=225)),
                ('purchaseledger', models.CharField(max_length=225)),
                ('itemname', models.CharField(max_length=225)),
                ('quantity', models.IntegerField()),
                ('rate', models.IntegerField()),
                ('amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('particualrs', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app1.tally_ledger')),
            ],
        ),
    ]
