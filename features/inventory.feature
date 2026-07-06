Feature: Inventory Manager

  Scenario: List all products in the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user lists all products
    Then the output should contain:
      | Product |
      | Coffee  |
      | Sugar   |