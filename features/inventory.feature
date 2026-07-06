Feature: Inventory Manager System

    Scenario: Add a product to an existing inventory
    Given the inventory contains products:
      | Product |
      | Apple   |
    When the user adds a product "Banana"
    Then the inventory should contain "Banana"


  Scenario: Search for a product that does not exist
    Given the inventory is empty
    When the user searches for the product "Mouse"
    Then the output should be "Product 'Mouse' not found."
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
