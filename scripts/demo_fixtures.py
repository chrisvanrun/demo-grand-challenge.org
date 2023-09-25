from pathlib import Path

from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

from grandchallenge.verifications.models import Verification
from django.core.files import File

DEMO_PATH = Path("/app/demo")
RESOURCE_PATH = DEMO_PATH / "resources"

USERNAMES_TYPE_A = ["Emma", "Olivia", "Ava", "Sophia", "Isabella"]
USERSNAMES_TYPE_B = ["Liam", "Noah", "William", "James", "Elijah"]


def _create_users(usernames):
    User = get_user_model()
    users = {}

    # Create user
    for username in usernames:
        if User.objects.filter(username=username).exists():
            users[username] = User.objects.get(username=username)
            continue
        user = User.objects.create(
            username=username,
            email=f"{username}@example.com",
            is_active=True,
        )
        user.set_password(username)
        user.save()

        EmailAddress.objects.create(
            user=user,
            email=user.email,
            verified=True,
            primary=True,
        )

        Verification.objects.create(
            user=user,
            email=user.email,
            is_verified=True,
        )
        user.user_profile.receive_newsletter = True
        user.user_profile.save()
        users[username] = user

    return users


def _upload_avatars(users):
    counts = {"a": 0, "b": 0}
    for username, user in users.items():
        if username in USERNAMES_TYPE_A:
            type_ = "a"
        else:
            type_ = "b"
        counts[type_] = counts[type_] + 1
        avatar_path = (
            RESOURCE_PATH / "avatars" / f"type_{type_}" / f"{counts[type_]}.png"
        )
        with open(avatar_path, "rb") as fd:
            user.user_profile.mugshot.save(
                f"{username}.png", content=File(fd), save=True
            )


def run():
    print("🔨 Creating demo users 🔨")

    users = _create_users(usernames=[*USERNAMES_TYPE_A, *USERSNAMES_TYPE_B])
    _upload_avatars(users)

    print("✨ Created demo users ✨")
