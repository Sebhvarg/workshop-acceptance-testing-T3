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


@when('the user searches for the product "{product}"')
def step_impl_search_product(context, product):
    # Llamamos a tu función search_product y guardamos el éxito y el mensaje
    context.success, context.output = context.inventory.search_product(product)

@then('the output should be "{message}"')
def step_impl_check_output(context, message):
    # Validamos que tu función haya retornado False
    assert context.success is False, "Se esperaba que la búsqueda fallara"
    # Validamos que el texto coincida exactamente con lo esperado
    assert context.output == message, f'Expected "{message}" but got "{context.output}"'
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
### Feature Eliminar ### 

# --- GIVEN STEPS ---

@given('the inventory contains products:')
def step_impl_given_products(context):
    context.inventory = Inventory()
    for row in context.table:
        product_name = row['Product']
        context.inventory.add_product(product_name, "Groceries", 5.0, 10)

# --- WHEN STEPS ---

@when('the user removes the product "{product_name}"')
def step_impl_remove_product(context, product_name):
    # Desempaquetamos la tupla que devuelve tu nueva lógica (success, msg)
    success, msg = context.inventory.remove_product(product_name)
    
    # Guardamos el mensaje en el contexto para poder validarlo en el "Then"
    context.output = msg

# --- THEN STEPS ---

@then('the inventory should not contain "{product_name}"')
def step_impl_should_not_contain(context, product_name):
    # Como self.products ahora es un diccionario, verificamos directamente si la llave existe
    assert product_name not in context.inventory.products, f"Error: '{product_name}' no fue eliminado del inventario."
