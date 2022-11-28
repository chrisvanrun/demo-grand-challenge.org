# Generated by Django 3.2.15 on 2022-11-28 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "workstation_configs",
            "0018_workstationconfiggroupobjectpermission_workstationconfiguserobjectpermission",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="workstationconfig",
            name="show_swivel_tool",
            field=models.BooleanField(
                default=False,
                help_text="A tool that allows swiveling the image around axes to view a custom orientation",
            ),
        ),
    ]
