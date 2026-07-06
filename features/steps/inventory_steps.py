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

### Feature Eliminar ### 

# --- GIVEN STEPS ---

@given('the inventory contains products:')
def step_impl_given_products(context):
    context.inventory = Inventory()
    
    # Adaptado para agregar productos a tu diccionario
    for row in context.table:
        product_name = row['Product']
        # Suponiendo que tu método de agregar recibe estos parámetros
        context.inventory.add_product(product_name, 5.0, 10, "Groceries")

@given('the inventory is empty')
def step_impl_empty_inventory(context):
    context.inventory = Inventory()

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

@then('the output should be "{message}"')
def step_impl_check_output(context, message):
    # Comparamos el mensaje esperado con el mensaje exacto que nos devolvió el método
    assert context.output == message, f"Se esperaba \"{message}\" pero se obtuvo \"{context.output}\""
