"""Functions to manage a users shopping cart items."""


def add_item(current_cart, items_to_add):
    """Add items to shopping cart.

    :param current_cart: dict - the current shopping cart.
    :param items_to_add: iterable - items to add to the cart.
    :return: dict - the updated user cart dictionary.
    """

    for item in items_to_add:
        if item in current_cart:
            current_cart[item] += 1
        else:
            current_cart[item] = 1
    return current_cart


def read_notes(notes):
    """Create user cart from an iterable notes entry.

    :param notes: iterable of items to add to cart.
    :return: dict - a user shopping cart dictionary.
    """

    return dict.fromkeys(notes, 1)


def update_recipes(ideas, recipe_updates):
    """Update the recipe ideas dictionary.

    :param ideas: dict - The "recipe ideas" dict.
    :param recipe_updates: dict - dictionary with updates for the ideas section.
    :return: dict - updated "recipe ideas" dict.
    """

    for recipe_name, recipe_content in recipe_updates:
        ideas[recipe_name] = recipe_content

    return ideas


def sort_entries(cart):
    """Sort a users shopping cart in alphabetically order.

    :param cart: dict - a users shopping cart dictionary.
    :return: dict - users shopping cart sorted in alphabetical order.
    """

    return dict(sorted(cart.items()))


def send_to_store(cart, isle_mapping):
    """Combine users order to isle and refrigeration information.

    :param cart: dict - users shopping cart dictionary.
    :param isle_mapping: dict - isle and refrigeration information dictionary.
    :return: dict - fulfillment dictionary ready to send to store.
    """
    fulfillment = {}
    for cart_item_name, cart_item_amount in cart.items():
        fulfillment_list = []
        fulfillment_list.append(cart_item_amount)
        fulfillment_list.extend(isle_mapping[cart_item_name])
        fulfillment.update({cart_item_name:fulfillment_list})

    return dict(sorted(fulfillment.items(), reverse=True))



def update_store_inventory(fulfillment_cart, store_inventory):
    """Update store inventory levels with user order.

    :param fulfillment cart: dict - fulfillment cart to send to store.
    :param store_inventory: dict - store available inventory
    :return: dict - store_inventory updated.
    """

    for item, fulfillment_list in fulfillment_cart.items():
        new_fulfillment_list = []
        if store_inventory[item][0] - fulfillment_cart[item][0] <= 0:
            new_fulfillment_list.append("Out of Stock")
        else:
            new_fulfillment_list.append(store_inventory[item][0] - fulfillment_cart[item][0])
        new_fulfillment_list.append(fulfillment_list[1])
        new_fulfillment_list.append(fulfillment_list[2])
        store_inventory.update({item:new_fulfillment_list})

    return store_inventory
