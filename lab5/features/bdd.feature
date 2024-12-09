Feature: Field extraction

  Scenario: Extracting a single field
    Given a list of goods
    When extract the title field
    Then a list

  Scenario: Extracting multiple fields
    Given a list of goods
    When extract the title and price fields
    Then a list of goods with title and price

  Scenario: Extracting a non-existent field
    Given a list of goods
    When extract a non-existent field
    Then an empty list

  Scenario: Getting all fields
    Given a list of goods
    When extract the title, price, color fields
    Then a list of goods with title, price, color


