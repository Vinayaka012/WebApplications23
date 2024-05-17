

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0005_auto_20191209_0000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='payapp.PaymentMethod'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('Bank', 'Bank Transfer'), ('Utilities', 'Bills & Utilities'), ('Transportation', 'Auto & Transport'), ('Groceries', 'Groceries'), ('Food', 'Food'), ('Shopping', 'Shopping'), ('Health', 'Healthcare'), ('Education', 'Education'), ('Travel', 'Travel'), ('Housing', 'Housing'), ('Entertainment', 'Entertainment'), ('Others', 'Others')], max_length=45),
        ),
    ]
