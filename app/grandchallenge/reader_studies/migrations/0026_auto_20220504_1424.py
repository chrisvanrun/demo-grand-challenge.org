# Generated by Django 3.2.13 on 2022-05-04 14:24

from django.db import migrations, models

import grandchallenge.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ("cases", "0008_delete_rawimagefile"),
        ("reader_studies", "0025_auto_20220503_1226"),
    ]

    operations = [
        migrations.AlterField(
            model_name="answer",
            name="images",
            field=models.ManyToManyField(
                null=True, related_name="answers", to="cases.Image"
            ),
        ),
        migrations.AlterField(
            model_name="readerstudy",
            name="hanging_list",
            field=models.JSONField(
                blank=True,
                default=list,
                null=True,
                validators=[
                    grandchallenge.core.validators.JSONValidator(
                        schema={
                            "$schema": "http://json-schema.org/draft-06/schema#",
                            "definitions": {},
                            "items": {
                                "$id": "#/items",
                                "additionalProperties": False,
                                "properties": {
                                    "denary": {
                                        "$id": "#/items/properties/denary",
                                        "default": "",
                                        "examples": ["im_denary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Denary Schema",
                                        "type": "string",
                                    },
                                    "denary-overlay": {
                                        "$id": "#/items/properties/denary-overlay",
                                        "default": "",
                                        "examples": ["im_denary-overlay.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Denary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "duodenary": {
                                        "$id": "#/items/properties/duodenary",
                                        "default": "",
                                        "examples": ["im_duodenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Duodenary Schema",
                                        "type": "string",
                                    },
                                    "duodenary-overlay": {
                                        "$id": "#/items/properties/duodenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_duodenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Duodenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "main": {
                                        "$id": "#/items/properties/main",
                                        "default": "",
                                        "examples": ["im_main.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Main Schema",
                                        "type": "string",
                                    },
                                    "main-overlay": {
                                        "$id": "#/items/properties/main-overlay",
                                        "default": "",
                                        "examples": ["im_main-overlay.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Main-Overlay Schema",
                                        "type": "string",
                                    },
                                    "nonary": {
                                        "$id": "#/items/properties/nonary",
                                        "default": "",
                                        "examples": ["im_nonary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Nonary Schema",
                                        "type": "string",
                                    },
                                    "nonary-overlay": {
                                        "$id": "#/items/properties/nonary-overlay",
                                        "default": "",
                                        "examples": ["im_nonary-overlay.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Nonary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "novemdenary": {
                                        "$id": "#/items/properties/novemdenary",
                                        "default": "",
                                        "examples": ["im_novemdenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Novemdenary Schema",
                                        "type": "string",
                                    },
                                    "novemdenary-overlay": {
                                        "$id": "#/items/properties/novemdenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_novemdenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Novemdenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "octodenary": {
                                        "$id": "#/items/properties/octodenary",
                                        "default": "",
                                        "examples": ["im_octodenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Octodenary Schema",
                                        "type": "string",
                                    },
                                    "octodenary-overlay": {
                                        "$id": "#/items/properties/octodenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_octodenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Octodenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "octonary": {
                                        "$id": "#/items/properties/octonary",
                                        "default": "",
                                        "examples": ["im_octonary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Octonary Schema",
                                        "type": "string",
                                    },
                                    "octonary-overlay": {
                                        "$id": "#/items/properties/octonary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_octonary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Octonary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "quaternary": {
                                        "$id": "#/items/properties/quaternary",
                                        "default": "",
                                        "examples": ["im_quaternary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Quaternary Schema",
                                        "type": "string",
                                    },
                                    "quaternary-overlay": {
                                        "$id": "#/items/properties/quaternary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_quaternary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Quaternary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "quattuordenary": {
                                        "$id": "#/items/properties/quattuordenary",
                                        "default": "",
                                        "examples": ["im_quattuordenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Quattuordenary Schema",
                                        "type": "string",
                                    },
                                    "quattuordenary-overlay": {
                                        "$id": "#/items/properties/quattuordenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_quattuordenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Quattuordenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "quinary": {
                                        "$id": "#/items/properties/quinary",
                                        "default": "",
                                        "examples": ["im_quinary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Quinary Schema",
                                        "type": "string",
                                    },
                                    "quinary-overlay": {
                                        "$id": "#/items/properties/quinary-overlay",
                                        "default": "",
                                        "examples": ["im_quinary-overlay.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Quinary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "quindenary": {
                                        "$id": "#/items/properties/quindenary",
                                        "default": "",
                                        "examples": ["im_quindenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Quindenary Schema",
                                        "type": "string",
                                    },
                                    "quindenary-overlay": {
                                        "$id": "#/items/properties/quindenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_quindenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Quindenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "secondary": {
                                        "$id": "#/items/properties/secondary",
                                        "default": "",
                                        "examples": ["im_secondary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Secondary Schema",
                                        "type": "string",
                                    },
                                    "secondary-overlay": {
                                        "$id": "#/items/properties/secondary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_secondary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Secondary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "senary": {
                                        "$id": "#/items/properties/senary",
                                        "default": "",
                                        "examples": ["im_senary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Senary Schema",
                                        "type": "string",
                                    },
                                    "senary-overlay": {
                                        "$id": "#/items/properties/senary-overlay",
                                        "default": "",
                                        "examples": ["im_senary-overlay.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Senary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "septenary": {
                                        "$id": "#/items/properties/septenary",
                                        "default": "",
                                        "examples": ["im_septenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Septenary Schema",
                                        "type": "string",
                                    },
                                    "septenary-overlay": {
                                        "$id": "#/items/properties/septenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_septenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Septenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "septendenary": {
                                        "$id": "#/items/properties/septendenary",
                                        "default": "",
                                        "examples": ["im_septendenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Septendenary Schema",
                                        "type": "string",
                                    },
                                    "septendenary-overlay": {
                                        "$id": "#/items/properties/septendenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_septendenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Septendenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "sexdenary": {
                                        "$id": "#/items/properties/sexdenary",
                                        "default": "",
                                        "examples": ["im_sexdenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Sexdenary Schema",
                                        "type": "string",
                                    },
                                    "sexdenary-overlay": {
                                        "$id": "#/items/properties/sexdenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_sexdenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Sexdenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "tertiary": {
                                        "$id": "#/items/properties/tertiary",
                                        "default": "",
                                        "examples": ["im_tertiary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Tertiary Schema",
                                        "type": "string",
                                    },
                                    "tertiary-overlay": {
                                        "$id": "#/items/properties/tertiary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_tertiary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Tertiary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "tredenary": {
                                        "$id": "#/items/properties/tredenary",
                                        "default": "",
                                        "examples": ["im_tredenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Tredenary Schema",
                                        "type": "string",
                                    },
                                    "tredenary-overlay": {
                                        "$id": "#/items/properties/tredenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_tredenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Tredenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "undenary": {
                                        "$id": "#/items/properties/undenary",
                                        "default": "",
                                        "examples": ["im_undenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Undenary Schema",
                                        "type": "string",
                                    },
                                    "undenary-overlay": {
                                        "$id": "#/items/properties/undenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_undenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Undenary-Overlay Schema",
                                        "type": "string",
                                    },
                                    "vigintenary": {
                                        "$id": "#/items/properties/vigintenary",
                                        "default": "",
                                        "examples": ["im_vigintenary.mhd"],
                                        "pattern": "^(.*)$",
                                        "title": "The Vigintenary Schema",
                                        "type": "string",
                                    },
                                    "vigintenary-overlay": {
                                        "$id": "#/items/properties/vigintenary-overlay",
                                        "default": "",
                                        "examples": [
                                            "im_vigintenary-overlay.mhd"
                                        ],
                                        "pattern": "^(.*)$",
                                        "title": "The Vigintenary-Overlay Schema",
                                        "type": "string",
                                    },
                                },
                                "required": ["main"],
                                "title": "The Items Schema",
                                "type": "object",
                            },
                            "title": "The Hanging List Schema",
                            "type": "array",
                        }
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="readerstudy",
            name="images",
            field=models.ManyToManyField(
                null=True, related_name="readerstudies", to="cases.Image"
            ),
        ),
        migrations.AlterField(
            model_name="readerstudy",
            name="use_display_sets",
            field=models.BooleanField(default=True, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name="readerstudy",
            name="validate_hanging_list",
            field=models.BooleanField(default=True, null=True),
        ),
    ]
