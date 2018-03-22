Feature: Bing search engine

  Scenario: User access to Bing homepage
    Given a Firefox navigator
    When the user access to Bing
    Then the homepage title says "Bing"

  Scenario: User tries to search something in Bing
    Given a Bing home page in Firefox
    When the user search for "Globant" using Bing
    Then the Bing engine returns more than 3 results