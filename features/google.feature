Feature: Google search engine

  Scenario: User access to Google homepage
    Given a Firefox navigator
    When the user access to Google
    Then the homepage title says "Google"

  Scenario: User tries to search something in Google
    Given a Google home page in Firefox
    When the user search for "Globant" using Google
    Then the Google engine returns more than 3 results
