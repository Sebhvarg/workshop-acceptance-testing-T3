from behave import given, when, then
from inventory import Inventory, Product

@given('the inventory contains products:')
def step_impl(context):
    context.inventory = Inventory()

    for row in context.table:
        product = Product(
            row["Product"],
            "General",
            1.0,
            10
        )
        context.inventory.products[product.name] = product

@when('the user lists all products')
def step_impl(context):
    context.output = context.inventory.list_products()

@then('the output should contain:')
def step_impl(context):
    product_names = [product.name for product in context.output]

    for row in context.table:
        assert row["Product"] in product_names