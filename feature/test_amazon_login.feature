Feature: Amazon.in Login

  @test
  Scenario: User logs in with valid credentials
    Given User is on the Amazon.in login page
    When User enters valid username and password
    Then User should be logged in successfully

  Scenario: User logs in with invalid credentials
    Given User is on the Amazon.in login page
    When User enters invalid username and password
    Then User should see an error message
