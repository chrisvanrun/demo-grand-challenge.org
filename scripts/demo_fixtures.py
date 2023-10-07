from pathlib import Path

from allauth.account.models import EmailAddress
from django.contrib.auth import get_user_model

from grandchallenge.cases.models import Image, ImageFile
from grandchallenge.challenges.models import Challenge
from grandchallenge.components.models import ComponentInterface, \
    ComponentInterfaceValue
from grandchallenge.core.fixtures import create_uploaded_image
from .development_fixtures import _create_algorithm_demo, _create_submissions
from grandchallenge.modalities.models import ImagingModality
from grandchallenge.reader_studies.models import DisplaySet, Question, \
    QuestionWidgetKindChoices, ReaderStudy
from grandchallenge.verifications.models import Verification
from django.core.files import File

from django.conf import settings

from grandchallenge.workstations.models import Workstation, WorkstationImage

DEMO_PATH = Path("/app/demo")
RESOURCE_PATH = DEMO_PATH / "resources"

USERNAMES_TYPE_A = ["Emma", "Olivia", "Ava", "Sophia", "Isabella", "demo"]
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


def _upload_workstation_image():
    w = Workstation.objects.get(title=settings.DEFAULT_WORKSTATION_SLUG)
    if w.workstationimage_set.count():
        print("🚗🏁 Skipping uploading workstation 🚗🏁")
        return

    workstation_path = RESOURCE_PATH / "viewers" / "CirrusCoreV2023_09_1.tar.gz"
    sha256sum = "cdb2e7d1260325487e61e8f02268d25e2d92b21a42aac01f21ad0b6a3c5494d9"

    if not workstation_path.exists():
        raise RuntimeError(
            f"Expected a saved container image: {workstation_path}. It is not version controlled. Make sure to add it manually to this clone"
        )

    with open(workstation_path, "rb") as fd:
        WorkstationImage.objects.create(
            workstation=w,
            image=File(fd),
            image_sha256=sha256sum,
        )

def _create_reader_studies(users, suffix):
    with open(RESOURCE_PATH / "miccai2023-logo.png", "rb") as fd:
        reader_study = ReaderStudy.objects.create(
            title=f"Demo Reader Study {suffix}",
            workstation=Workstation.objects.last(),
            logo=File(fd),
            description="Demo reader study",
            view_content={"main": ["generic-medical-image"]},
            allow_case_navigation=True,
            allow_show_all_annotations=True,
        )
    reader_study.editors_group.user_set.add(users["demo"])
    reader_study.readers_group.user_set.add(users["James"], users["Emma"])

    Question.objects.create(
        reader_study=reader_study,
        question_text="A text-type question",
        answer_type=Question.AnswerType.TEXT,
        widget=QuestionWidgetKindChoices.TEXT_AREA
    )
    Question.objects.create(
        reader_study=reader_study,
        question_text="A range-type question",
        answer_type=Question.AnswerType.NUMBER,
        answer_min_value=0,
        answer_max_value=100,
        answer_step_size=1,
        widget=QuestionWidgetKindChoices.NUMBER_RANGE

    )
    Question.objects.create(
        reader_study=reader_study,
        question_text="A mask-type question",
        answer_type=Question.AnswerType.MASK,
        image_port="main",
    )
    Question.objects.create(
        reader_study=reader_study,
        question_text="A bounding-box-type question",
        answer_type=Question.AnswerType.MULTIPLE_2D_BOUNDING_BOXES,
        image_port="main",
    )

    display_set = DisplaySet.objects.create(reader_study=reader_study)
    image = Image(
        name="prostate.mha",
        modality=ImagingModality.objects.get(modality="CT"),
        width=128,
        height=128,
        color_space="RGB",
    )
    image.save()
    with open(RESOURCE_PATH / "prostate.mha", 'rb') as fd:
        ImageFile.objects.create(image=image, file=File(fd))

    image.save()
    civ = ComponentInterfaceValue.objects.create(
        interface=ComponentInterface.objects.get(slug="generic-medical-image"),
        image=image,
    )
    display_set.values.set([civ, civ, civ])

def run():
    users = _create_users(usernames=[*USERNAMES_TYPE_A, *USERSNAMES_TYPE_B])
    _upload_avatars(users)
    print("🔨 Created demo users 🔨")

    _upload_workstation_image()
    print("🔨 Uploaded workstation 🔨")


    _create_reader_studies(users, suffix=ReaderStudy.objects.count())

    demo_challenge = Challenge.objects.get(short_name="demo")

    demo_challenge.update_user_forum_permissions()
    for username, user in users.items():
        print(f"🔨 Creating algorithm + submission for {username} 🔨")
        demo_challenge.add_participant(user)
        algorithm = _create_algorithm_demo(
            creator=user,
            editors_group=[user],
            users_group=[],
        )
        _create_submissions(challenge=demo_challenge, user=user,
                            algorithm=algorithm)
    print("✨ Finished setting up demo ✨")
