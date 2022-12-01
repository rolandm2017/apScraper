from celery import Celery
import pytest

from ..config import Config

from canadaAps.scraper.ProgramInit import create_app


def client(cel_instance_to_satisfy_argument):
    app = create_app(cel_instance_to_satisfy_argument)
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client


@pytest.mark.skip(reason="done with postman")
def test_one_shot_rent_canada():
    response = client.post("/", json={
        "provider": "rentCanada",
        "id": 0,
        "lat": 45.5019,
        "long":-73.5674,
        "zoomWidth": 10
    })
    assert len(response.results.listings) > 5


@pytest.mark.skip(reason="done with postman")
def test_one_shot_rent_faster():
    response = client.post("/", json={
        "provider": "rentFaster",
        "id": 0,
        "lat": 45.5019,
        "long": -73.5674,
        "zoomWidth": 10
    })
    assert len(response.results.listings) > 5


@pytest.mark.skip(reason="done with postman")
def test_one_shot_rent_seeker():
    response = client.post("/", json={
        "provider": "rentSeeker",
        "id": 0,
        "lat": 45.5019,
        "long":-73.5674,
        "zoomWidth": 10
    })
    assert len(response.results.listings) > 5

