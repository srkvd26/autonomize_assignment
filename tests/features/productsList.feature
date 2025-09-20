Feature: Fetching title, price, rating & reviews details of the products from the amazon page

  Scenario: Get details of the products from the search results for "mobile" keyword
    Given the user is on the amazon home page
    When user search with the keyword
    Then extract details of the products from the first 2 pages
    And save the details into an Excel file
    And check if details of atleast 10 products are fetched