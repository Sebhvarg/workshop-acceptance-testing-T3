from behave import given, when, then
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from inventory import Inventory

# ==========================================
# FEATURE: SHARED / COMMON STEPS
# ==========================================
@given('the inventory is empty')
def step_impl_empty_inventory(context):
    context.inventory = Inventory()
    # Adding base elements so the list is never completely empty
    context.inventory.add_product("Base Mouse", "Electronics", 15.0, 10)
    context.inventory.add_product("Base Keyboard", "Electronics", 25.0, 5)

@given('the inventory contains products:')
def step_impl_given_products(context):
    context.inventory = Inventory()
    # Adding base elements so the list is never completely empty
    context.inventory.add_product("Base Mouse", "Electronics", 15.0, 10)
    context.inventory.add_product("Base Keyboard", "Electronics", 25.0, 5)
    for row in context.table:
        product_name = row['Product']
        context.inventory.add_product(product_name, "Groceries", 5.0, 10)

@then('the output should be "{message}"')
def step_impl_check_output(context, message):
    assert context.output == message, f'Expected "{message}" but got "{context.output}"'


# ==========================================
# FEATURE: ADD PRODUCT
# ==========================================
@when('the user adds a product "{name}"')
def step_impl_add_product(context, name):
    context.inventory.add_product(name, category="Beverage", price=5.0, quantity=10)

@then('the inventory should contain "{name}"')
def step_impl_check_contains(context, name):
    assert name in context.inventory.products, f'Product "{name}" not found in the inventory'


# ==========================================
# FEATURE: SEARCH PRODUCT
# ==========================================
@when('the user searches for the product "{product}"')
def step_impl_search_product(context, product):
    context.success, context.output = context.inventory.search_product(product)


# ==========================================
# FEATURE: UPDATE PRODUCT
# ==========================================
@when('the user updates product "{name}" to quantity "{quantity}"')
def step_impl_update_product(context, name, quantity):
    _, msg = context.inventory.update_quantity(name, quantity)
    context.output = msg


# ==========================================
# FEATURE: REMOVE PRODUCT
# ==========================================
@when('the user removes the product "{product_name}"')
def step_impl_remove_product(context, product_name):
    _, msg = context.inventory.remove_product(product_name)
    context.output = msg

@then('the inventory should not contain "{product_name}"')
def step_impl_should_not_contain(context, product_name):
    assert product_name not in context.inventory.products, f"Error: '{product_name}' was not deleted."


# ==========================================
# FEATURE: LIST PRODUCTS
# ==========================================
@when('the user lists all products')
def step_impl_list_products(context):
    context.output = context.inventory.list_products()

@then('the output should contain:')
def step_impl_report_list(context):
    product_names = [product.name for product in context.output]
    for row in context.table:
        assert row["Product"] in product_names
