# Generated by Django 3.1.5 on 2021-02-15 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailadmin', '0002_admin'),
    ]

    operations = [
        migrations.DeleteModel(name='Admin'),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'permissions': [('access_admin', 'Can access Wagtail admin')],
                'default_permissions': [],
            },
        ),
    ]