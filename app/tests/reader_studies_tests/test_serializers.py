import pytest

from grandchallenge.reader_studies.models import QuestionWidgetKindChoices
from grandchallenge.reader_studies.serializers import QuestionSerializer
from tests.reader_studies_tests.factories import QuestionFactory


@pytest.mark.django_db
def test_widget_on_question_serializer(rf):
    qu = QuestionFactory()
    serializer = QuestionSerializer(qu, context={"request": rf.get("/foo")})
    assert not serializer.data["widget"]
    qu.widget = QuestionWidgetKindChoices.ACCEPT_REJECT
    qu.save()
    serializer2 = QuestionSerializer(qu, context={"request": rf.get("/foo")})
    assert (
        serializer2.data["widget"]
        == QuestionWidgetKindChoices.ACCEPT_REJECT.label
    )
