# Generated by Django 4.2.2 on 2023-08-07 08:15

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("testapp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="items",
            name="itemcost",
        ),
    ]