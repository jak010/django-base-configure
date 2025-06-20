import os

# import django
import pytest
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.config.settings.local")
# django.setup()


@pytest.fixture
def django_db_setup():
    """ 테스트용 DB를 생성하지 않도록 처리 """
    pass
