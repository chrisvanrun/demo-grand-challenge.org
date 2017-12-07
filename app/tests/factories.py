import factory
import hashlib
from django.conf import settings

from comicmodels.models import ComicSite
from evaluation.models import Submission, Job, Method, Result

SUPER_SECURE_TEST_PASSWORD = 'testpasswd'


class ChallengeFactory(factory.DjangoModelFactory):
    class Meta:
        model = ComicSite

    short_name = factory.Sequence(lambda n: f'test_challenge_{n}')


class UserFactory(factory.DjangoModelFactory):
    class Meta:
        model = settings.AUTH_USER_MODEL

    username = factory.Sequence(lambda n: 'test_user_%s' % n)
    email = factory.LazyAttribute(lambda u: '%s@test.com' % u.username)
    password = factory.PostGenerationMethodCall('set_password', SUPER_SECURE_TEST_PASSWORD)

    is_active = True
    is_staff = False
    is_superuser = False


class SubmissionFactory(factory.DjangoModelFactory):
    class Meta:
        model = Submission

    challenge = factory.SubFactory(ChallengeFactory)
    file = factory.django.FileField()


class JobFactory(factory.DjangoModelFactory):
    class Meta:
        model = Job

def hash_sha256(s):
    m = hashlib.sha256()
    m.update(s.encode())
    return f'sha256:{m.hexdigest()}'

class MethodFactory(factory.DjangoModelFactory):
    class Meta:
        model = Method

    challenge = factory.SubFactory(ChallengeFactory)
    image = factory.django.FileField()
    image_sha256 = factory.sequence(lambda n: hash_sha256(f'image{n}'))

class ResultFactory(factory.DjangoModelFactory):
    class Meta:
        model = Result
