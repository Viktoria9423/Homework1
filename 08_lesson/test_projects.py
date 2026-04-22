import pytest
from api_client import YougileAPI


@pytest.fixture
def api():
    return YougileAPI()


def test_create_project_positive(api):
    response = api.create_project("Test Project")

    assert response.status_code in [200, 201]

    data = response.json()
    assert "id" in data


def test_create_project_negative(api):
    response = api.create_project("")

    assert response.status_code in [400, 422]


def test_update_project_positive(api):
    create = api.create_project("Temp")
    project_id = create.json().get("id")

    assert project_id is not None

    response = api.update_project(project_id, "Updated name")

    assert response.status_code in [200, 204]


def test_update_project_negative(api):
    response = api.update_project("wrong_id", "Test")

    assert response.status_code in [400, 404, 401]


def test_get_project_positive(api):
    create = api.create_project("Temp2")
    project_id = create.json().get("id")

    assert project_id is not None

    response = api.get_project(project_id)

    assert response.status_code == 200


def test_get_project_negative(api):
    response = api.get_project("invalid_id")

    assert response.status_code in [400, 404, 401]
