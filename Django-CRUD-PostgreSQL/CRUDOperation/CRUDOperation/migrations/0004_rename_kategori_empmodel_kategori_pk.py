# Generated by Django 4.1.2 on 2023-02-22 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("CRUDOperation", "0003_alter_kategorimodel_table"),
    ]

    operations = [
        migrations.RenameField(
            model_name="empmodel",
            old_name="kategori",
            new_name="kategori_pk",
        ),
    ]
