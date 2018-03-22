Feature: Search engines comparison

  Scenario: User tries to search something in Google & Bing
    Given a Google home page in Firefox
    And a Bing home page in Firefox
    When the user search for "Globant" using Google
    And the user search for "Globant" using Bing
    Then the Google engine returns more than 3 results
    And the Bing engine returns more than 3 results
    And Bing returns more results than Google
    And the first result in Bing is not the same as in Google
