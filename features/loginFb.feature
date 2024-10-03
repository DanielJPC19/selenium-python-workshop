Feature: Login Intu Feature
  Scenario: Successful login with valid credentials
    Given the user is on the login intu page
    When the user logs in intu with valid credentials
    Then the user should be redirected to the dashboard page