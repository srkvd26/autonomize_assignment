Feature: Adding users and performing CRUD operations using API

  Scenario: Creating users from Excel
    Given The data is fetched from Excel
    When Create the users using the POST request
    Then All the users fetched from excel should get successfully created

  Scenario: Update a user's phone and email
    Given The users are created from Excel
    When Update the first user's phone and email
    Then phone and email of respective user are updated

  Scenario: Get details of a created user
    Given The users are created from Excel
    When Get second user details
    Then Fetched details should match the created data

  Scenario: Delete a user
    Given The users are created from Excel
    When Delete the last user
    Then The user should no longer exist
