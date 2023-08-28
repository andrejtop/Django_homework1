import pytest
from model_bakery import baker
from rest_framework.test import APIClient
from django.urls import reverse
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory

@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory




@pytest.mark.django_db
def test_get_first_course(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse("courses-detail", args=[courses[0].id])
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data.get('id') == courses[0].id
    assert data.get('name') == courses[0].name

@pytest.mark.django_db
def test_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)
    url = reverse("courses-list")
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 10

@pytest.mark.django_db
def test_filter_courses_by_id(client, course_factory):
    course = course_factory(_quantity=10)
    query_params = {'id': course[5].id}
    url = reverse("courses-list")
    response = client.get(url, params=query_params)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 10
    assert data[5]['id'] == course[5].id


@pytest.mark.django_db
def test_filter_courses_by_name(client, course_factory):
    course = course_factory(_quantity=10)
    query_params = {'name': course[5].name}
    url = reverse("courses-list")
    response = client.get(url, params=query_params)
    data = response.json()
    assert response.status_code == 200
    assert len(data) == 10
    assert data[5]['name'] == course[5].name

@pytest.mark.django_db
def test_create_course(client):
    url = reverse("courses-list")
    response = client.post(url, {"name": "Программирование"})
    assert response.status_code == 201
    assert response.data["name"] == "Программирование"

@pytest.mark.django_db
def test_update_course(client, course_factory):
    course = course_factory(name='математика')
    update_data = {'name': 'Физика'}
    url = reverse("courses-detail", args=[course.id])
    response = client.patch(url, update_data)
    assert response.status_code == 200
    assert response.json()['name'] == 'Физика'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    course = course_factory(name='Math', students=[])
    url = reverse("courses-detail", args=[course.id])
    response = client.delete(url)
    assert response.status_code == 204


