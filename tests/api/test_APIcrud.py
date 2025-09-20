import pytest
import requests
from pytest_bdd import *
from utils.excelReadWrite import ExcelReadWrite
from utils.configReader import ConfigReader

scenarios("../features/apiCRUD.feature")

config = ConfigReader()
base_url = config.get("api", "base_url") + "/users"


@given("The data is fetched from Excel")
def load_users_from_excel():
    pytest.userDetails = ExcelReadWrite.read("data/usersDetails.xlsx")


@when("Create the users using the POST request")
def create_users():
    createdUsers = []
    for user in pytest.userDetails:
        response = requests.post(f"{base_url}/add", json=user)
        assert response.status_code == 201
        data = response.json()
        createdUsers.append(data)
    pytest.createdUsers = createdUsers


@then("All the users fetched from excel should get successfully created")
def validate_creation():
    assert len(pytest.createdUsers) == len(pytest.userDetails)



@given("The users are created from Excel")
def users_created():
    assert hasattr(pytest, "createdUsers")


@when("Update the first user's phone and email")
def update_user():
    userId = pytest.createdUsers[0]["id"]
    payload = {
        "phone": "9898989898",
        "email": "xyz123@test.com"
    }
    response = requests.patch(f"{base_url}/{userId}", json=payload)
    assert response.status_code == 200
    pytest.updatedUser = response.json()


@then("phone and email details of the respective user are updated")
def validate_update():
    assert pytest.updatedUser["phone"] == "9898989898"
    assert pytest.updatedUser["email"] == "xyz123@test.com"



@when("Get second user details")
def get_user():
    userId = pytest.createdUsers[1]["id"]
    response = requests.get(f"{base_url}/{userId}")
    assert response.status_code == 200
    pytest.fetchedUser = response.json()


@then("Fetched details should match the created data")
def validate_fetched_user():
    for key in ["firstName", "lastName", "age"]:
        assert pytest.fetchedUser[key] == pytest.createdUsers[1][key]


@when("Delete the last user")
def delete_user():
    userId = pytest.createdUsers[-1]["id"]
    response = requests.delete(f"{base_url}/{userId}")
    assert response.status_code == 200
    pytest.deletedUserId = userId


@then("The user should no longer exist")
def validate_deletion():
    response = requests.get(f"{base_url}/{pytest.deletedUserId}")
    assert response.status_code == 404