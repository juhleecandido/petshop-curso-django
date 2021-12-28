# Generated by Django 4.0 on 2021-12-28 00:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('core', '0004_rename_distribuidora_racao_distribuidora_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'Carrinho'), (2, 'Realizado'), (3, 'Pago'), (4, 'Entregue')], default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='compras', to='auth.user')),
            ],
        ),
    ]
