from behave import given, when, then
import sys
import os


sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from inventory import Inventory

@given('the inventory is empty')
def step_impl_empty_inventory(context):
    context.inventory = Inventory()

@when('the user adds a product "{name}"')
def step_impl_add_product(context, name):
    
    context.inventory.add_product(name, category="Beverage", price=5.0, quantity=10)

@then('the inventory should contain "{name}"')
def step_impl_check_contains(context, name):
    assert name in context.inventory.products, f'Product "{name}" not found in the inventory'
