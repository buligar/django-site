# Generated by Django 4.0.2 on 2022-03-14 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('melanomas', '0002_alter_articles_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('cover', models.ImageField(upload_to='images/')),
                ('book', models.FileField(upload_to='books/')),
            ],
        ),
    ]
