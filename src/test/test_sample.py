import pytest
from apps.models import Sample
from django.test import override_settings


@override_settings(DEBUG=True)
@pytest.mark.django_db
def test_sample():
    sample = Sample.objects.create(desc="test")

    print(sample)

    assert sample.desc == "test"
