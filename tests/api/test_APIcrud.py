import pytest
import requests
from pytest_bdd import *
from utils.excelReadWrite import ExcelReadWrite
from utils.configReader import ConfigReader

scenarios("../features/apiCRUD.feature")

config = ConfigReader()
base_url = config.get("api", "base_url") + "/users"


@given("The data is fetched from Excel")
def load_users_from_excel(logger):
    pytest.userDetails = ExcelReadWrite.read("data/usersDetails.xlsx")
    logger.info(f"Fetched {len(pytest.userDetails)} users from Excel")


@when("Create the users using the POST request")
def create_users(logger):
    createdUsers = []
    for user in pytest.userDetails:
        response = requests.post(f"{base_url}/add", json=user)
        logger.info(f"POST {base_url}/add - Status: {response.status_code}")
        assert response.status_code == 201
        data = response.json()
        createdUsers.append(data)
    pytest.createdUsers = createdUsers
    logger.info(f"Created {len(pytest.createdUsers)} users successfully")


@then("All the users fetched from excel should get successfully created")
def validate_creation(logger):
    assert len(pytest.createdUsers) == len(pytest.userDetails)
    logger.info("All users created successfully")


@given("The users are created from Excel")
def users_created(logger):
    assert hasattr(pytest, "createdUsers")
    logger.info("Users are already created")


@when("Update the first user's phone and email")
def update_user(logger):
    userId = pytest.createdUsers[0]["id"]
    payload = {"phone": "9898989898", "email": "xyz123@test.com"}
    response = requests.patch(f"{base_url}/{userId}", json=payload)
    logger.info(f"PATCH {base_url}/{userId} - Status: {response.status_code}")
    assert response.status_code == 200
    pytest.updatedUser = response.json()


@then("phone and email details of the respective user are updated")
def validate_update(logger):
    assert pytest.updatedUser["phone"] == "9898989898"
    assert pytest.updatedUser["email"] == "xyz123@test.com"
    logger.info("User phone and email updated successfully")


@when("Get second user details")
def get_user(logger):
    userId = pytest.createdUsers[1]["id"]
    response = requests.get(f"{base_url}/{userId}")
    logger.info(f"GET {base_url}/{userId} - Status: {response.status_code}")
    assert response.status_code == 200
    pytest.fetchedUser = response.json()


@then("Fetched details should match the created data")
def validate_fetched_user(logger):
    for key in ["firstName", "lastName", "age"]:
        assert pytest.fetchedUser[key] == pytest.createdUsers[1][key]
    logger.info("Fetched user details match with the created data")


@when("Delete the last user")
def delete_user(logger):
    userId = pytest.createdUsers[-1]["id"]
    response = requests.delete(f"{base_url}/{userId}")
    logger.info(f"DELETE {base_url}/{userId} - Status: {response.status_code}")
    assert response.status_code == 200
    pytest.deletedUserId = userId


@then("The user should no longer exist")
def validate_deletion(logger):
    response = requests.get(f"{base_url}/{pytest.deletedUserId}")
    logger.info(f"GET {base_url}/{pytest.deletedUserId} - Status: {response.status_code}")
    assert response.status_code == 404
    logger.info("User deletion verified successfully")
