Feature: Inventory Manager
  
  Scenario: Add a product to the inventory
    Given the inventory is empty
    When the user adds a product "Coffee"
    Then the inventory should contain "Coffee"


  Scenario: Search for a product that does not exist
    Given the inventory is empty
    When the user searches for the product "Mouse"
    Then the output should be "Product 'Mouse' not found."