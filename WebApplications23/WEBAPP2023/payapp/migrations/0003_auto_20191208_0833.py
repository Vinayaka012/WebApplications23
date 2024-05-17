

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0002_create_groups'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.CharField(choices=[('Credit', 'Credit Card'), ('Debit', 'Debit Card')], max_length=45),
        ),
        migrations.AlterField(
            model_name='paymentmethod',
            name='method_type',
            field=models.CharField(default='', max_length=255),
        ),
    ]
