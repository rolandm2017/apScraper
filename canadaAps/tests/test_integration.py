from celery import Celery
import pytest

from ..config import Config

from canadaAps.scrapers.ProgramInit import create_app

# from flaskr import flaskr


# @pytest.fixture
# def client():
#     db_fd, flaskr.app.config['DATABASE'] = tempfile.mkstemp()
#     flaskr.app.config['TESTING'] = True
#
#     with flaskr.app.test_client() as client:
#         with flaskr.app.app_context():
#             flaskr.init_db()
#         yield client
#
#     os.close(db_fd)
#     os.unlink(flaskr.app.config['DATABASE'])

celery = Celery("integrationTest", broker=Config.CELERY_BROKER_URL, result_backend=Config.RESULT_BACKEND)


def client(cel_instance_to_satisfy_argument):
    app = create_app(cel_instance_to_satisfy_argument)
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


# @pytest.mark.skip(reason="uses external api - dont wanna run it every time")
def test_one_shot_rent_canada():
    response = client.post("/", json={
        "provider": "rentCanada",
        "id": 0,
        "lat": 45.5019,
        "long":-73.5674,
        "zoomWidth": 10
    })
    assert len(response.results.listings) > 5


# @pytest.mark.skip(reason="uses external api - dont wanna run it every time")
def test_one_shot_rent_faster():
    response = client.post("/", json={
        "provider": "rentFaster",
        "id": 0,
        "lat": 45.5019,
        "long": -73.5674,
        "zoomWidth": 10
    })
    assert len(response.results.listings) > 5


# @pytest.mark.skip(reason="uses external api - dont wanna run it every time")
def test_one_shot_rent_seeker():
    response = client.post("/", json={
        "provider": "rentSeeker",
        "id": 0,
        "lat": 45.5019,
        "long":-73.5674,
        "zoomWidth": 10
    })
    assert len(response.results.listings) > 5

