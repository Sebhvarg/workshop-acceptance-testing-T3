Feature: Inventory Manager System

  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"

  Scenario: Update a product that does not exist
    Given the inventory is empty
    When the user updates product "Tea" to quantity "20"
    Then the output should be "Product 'Tea' not found."
  Scenario: Remove a product from the inventory
    Given the inventory contains products:
      | Product |
      | Coffee  |
      | Sugar   |
    When the user removes the product "Coffee"
    Then the inventory should not contain "Coffee"

  Scenario: Remove a product that does not exist
    Given the inventory is empty
    When the user removes the product "Coffee"
    Then the output should be "Product 'Coffee' not found."
