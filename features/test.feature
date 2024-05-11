Feature: Google Search
  As a user
  I want to search for a term on Google
  So that I can find relevant information

  Scenario: Searching for "automation testing"
    Given I am on the Google homepage
    When I search for "automation testing"
    Then I should see search results related to "automation testing"