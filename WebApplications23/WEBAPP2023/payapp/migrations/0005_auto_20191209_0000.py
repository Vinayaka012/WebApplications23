

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0004_remove_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='payment_method',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='payment_method', to='payapp.PaymentMethod'),
        ),
    ]
