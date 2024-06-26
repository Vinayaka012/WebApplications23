

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('method_id', models.AutoField(primary_key=True, serialize=False)),
                ('method_type', models.CharField(choices=[('account', 'Easy Pay Account'), ('card', 'Cards'), ('bank', 'Bank')], default=None, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='payment_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transaction_id', models.AutoField(primary_key=True, serialize=False)),
                ('transaction_type', models.CharField(choices=[('send', 'Send'), ('request', 'Request'), ('transfer', 'Transfer')], default='', max_length=45)),
                ('category', models.CharField(choices=[('bank', 'Bank Transfer'), ('utilities', 'Bills & Utilities'), ('transportation', 'Auto & Transport'), ('groceries', 'Groceries'), ('shopping', 'Shopping'), ('health', 'Healthcare'), ('education', 'Education'), ('travel', 'Travel'), ('housing', 'Housing'), ('entertainment', 'Entertainment'), ('others', 'Others')], max_length=45)),
                ('amount', models.FloatField(default=0.0)),
                ('description', models.CharField(default=False, max_length=200)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('is_complete', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('payment_method', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='payment_method', to='payapp.PaymentMethod')),
                ('receiver', models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='receiver', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('birthday', models.DateField(default=None)),
                ('address', models.CharField(default=None, max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Friendship',
            fields=[
                ('friendship_id', models.AutoField(primary_key=True, serialize=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friendship_creator', to=settings.AUTH_USER_MODEL)),
                ('friend', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='friend', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField(default=0.0)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payapp.PaymentMethod')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(choices=[('credit', 'Credit Card'), ('debit', 'Debit Card')], max_length=45)),
                ('card_number', models.CharField(default=None, max_length=16)),
                ('owner_first_name', models.CharField(max_length=45)),
                ('owner_last_name', models.CharField(max_length=45)),
                ('security_code', models.CharField(default=None, max_length=3)),
                ('expiration_date', models.DateField(default=None)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payapp.PaymentMethod')),
            ],
            options={
                'ordering': ['card_type', 'card_number'],
                'unique_together': {('card_type', 'owner_first_name', 'owner_last_name', 'card_number', 'security_code', 'expiration_date')},
            },
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_first_name', models.CharField(default=None, max_length=255)),
                ('owner_last_name', models.CharField(default=None, max_length=255)),
                ('routing_number', models.CharField(default=None, max_length=9)),
                ('account_number', models.CharField(default=None, max_length=10)),
                ('payment', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='payapp.PaymentMethod')),
            ],
            options={
                'unique_together': {('routing_number', 'account_number')},
            },
        ),
    ]
