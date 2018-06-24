def display_inventory(dic):
    print('Inventory:')
    total = 0
    for k, v in dic.items():
        print(v, k)
        total += v
    print('Total number of items: {}'.format(total))


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
display_inventory(stuff)


def add_to_inventory(inventory, added_items):
    for item in added_items:
        inventory[item] = inventory.get(item, 0) + 1
    return inventory


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = add_to_inventory(inv, dragonLoot)
display_inventory(inv)
