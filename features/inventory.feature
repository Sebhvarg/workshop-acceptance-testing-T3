Feature: Inventory Manager
  
  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"

  Scenario: Update a product that does not exist
    Given the inventory is empty
    When the user updates product "Tea" to quantity "20"
    Then the output should be "Product 'Tea' not found."