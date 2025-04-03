from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('finanz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='finanz.category'),
        ),
    ]
