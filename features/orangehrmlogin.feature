Feature: OrangeHRM Login
  Scenario: Login to orangeHRM with valid parameters
    Given I launch chrome browser
    When I open orange HRM Homepage
    And Enter username "admin" and password "admin123"
    And click on login button
    Then user must successfully login to the Dashboard page
    
