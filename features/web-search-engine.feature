# Created by javiersorella at 21/03/18
Feature: Google search engine
  # Enter feature description here

  Scenario: User access to Google homepage
    Given a Firefox navigator
    When the user access to Google
    Then the homepage title says "Google"

  Scenario: User tries to search something in Google
    Given a Google home page in Firefox
    When the user searchs for "Globant"
    Then the engine returns more than 3 results
