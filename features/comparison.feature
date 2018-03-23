Feature: Search engines comparison

  Scenario: User tries to search something in Google & Bing
    Given two web search engines: Google and Bing
    When the user search for "Globant" in Google and Bing
    Then Bing returns more results than Google
    And the first result in Bing is not the same as in Google
