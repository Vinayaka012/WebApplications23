

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payapp', '0003_auto_20191208_0833'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Friendship',
        ),
    ]
