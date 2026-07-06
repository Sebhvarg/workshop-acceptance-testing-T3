from behave import given, when, then
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from inventory import Inventory

# --- Scenario: Add a product to the inventory ---

#Step 1: Given the inventory is empty
@given('the inventory is empty')
def step_impl_empty_inventory(context):
    context.inventory = Inventory()

#Step 2: When the user adds a product "{name}"
@when('the user adds a product "{name}"')
def step_impl_add_product(context, name):
    context.inventory.add_product(name, category="Beverage", price=5.0, quantity=10)

#Step 3: Then the inventory should contain "{name}"
@then('the inventory should contain "{name}"')
def step_impl_check_contains(context, name):
    assert name in context.inventory.products, f'Product "{name}" not found in the inventory'


# --- Scenario: Update a product that does not exist ---

#Step 1: Given the inventory is empty

#Step 2: When the user updates product "{name}" to quantity "{quantity}"
@when('the user updates product "{name}" to quantity "{quantity}"')
def step_impl_update_product(context, name, quantity):
    success, msg = context.inventory.update_quantity(name, quantity)
    context.output = msg

#Step 3: Then the output should be "{message}"
@then('the output should be "{message}"')
def step_impl_check_output(context, message):
    assert context.output == message, f'Expected "{message}" but got "{context.output}"'