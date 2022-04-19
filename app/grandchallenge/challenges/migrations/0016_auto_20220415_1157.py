# Generated by Django 3.2.13 on 2022-04-15 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("challenges", "0015_auto_20220412_1038"),
    ]

    operations = [
        migrations.AddField(
            model_name="challengerequest",
            name="algorithm_inputs",
            field=models.TextField(
                blank=True,
                help_text="What are the inputs to the algorithms submitted as solutions to your Type 2 challenge going to be? Please describe in detail what the input(s) reflect(s), for example, MRI scan of the brain, or chest X-ray. Grand Challenge only supports .mha and .tiff image files and json files for algorithms.",
            ),
        ),
        migrations.AddField(
            model_name="challengerequest",
            name="algorithm_outputs",
            field=models.TextField(
                blank=True,
                help_text="What are the outputs to the algorithms submitted as solutions to your Type 2 challenge going to be? Please describe in detail what the output(s) reflect(s), for example, probability of a positive PCR result, or stroke lesion segmentation. ",
            ),
        ),
    ]
