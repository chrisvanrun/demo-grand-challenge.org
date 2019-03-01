from rest_framework import serializers
from django.conf import settings


def validate_grader_is_current_retina_user(grader, context):
    """
    This method checks if the passed grader equals the request.user that is passed in the context.
    Only applies to users that are in the retina_graders group.
    """
    request = context.get("request")
    if request and request.user.is_authenticated:
        user = request.user
        if user.groups.filter(
            name=settings.RETINA_GRADERS_GROUP_NAME
        ).exists():
            if grader != user:
                raise serializers.ValidationError(
                    "User is not allowed to create annotation for other grader"
                )
