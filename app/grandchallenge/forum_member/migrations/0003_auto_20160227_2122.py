# Generated by Django 1.9.2 on 2016-02-27 20:22
import machina.core.validators
import machina.models.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("forum_member", "0002_auto_20160225_0515"),
    ]

    operations = [
        migrations.AlterField(
            model_name="forumprofile",
            name="signature",
            field=machina.models.fields.MarkupTextField(
                blank=True,
                no_rendered_field=True,
                null=True,
                validators=[
                    machina.core.validators.NullableMaxLengthValidator(255)
                ],
                verbose_name="Signature",
            ),
        ),
    ]
