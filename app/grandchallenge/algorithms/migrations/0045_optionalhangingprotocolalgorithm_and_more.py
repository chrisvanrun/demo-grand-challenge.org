# Generated by Django 4.1.10 on 2023-08-28 08:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("hanging_protocols", "0010_alter_hangingprotocol_json"),
        ("algorithms", "0044_algorithmimage_size_in_registry_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OptionalHangingProtocolAlgorithm",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "algorithm",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="algorithms.algorithm",
                    ),
                ),
                (
                    "hanging_protocol",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="hanging_protocols.hangingprotocol",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="algorithm",
            name="optional_hanging_protocols",
            field=models.ManyToManyField(
                blank=True,
                help_text="Optional alternative hanging protocols for this algorithm",
                related_name="optional_for_algorithm",
                through="algorithms.OptionalHangingProtocolAlgorithm",
                to="hanging_protocols.hangingprotocol",
            ),
        ),
    ]
