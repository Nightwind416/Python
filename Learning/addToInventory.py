def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        item_total = item_total + v
    print("Total number of items: " + str(item_total))


def addToInventory(inventory, addedItems):
    for i in addedItems:
        if i in inventory:
#             print('adding count')
            inventory[i] += 1
        else:
            inventory[i] = 1
#             print('adding new')
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)


# Output answer
# 
# Inventory:
# 45 gold coin
# 1 rope
# 1 ruby
# 1 dagger
# 
# Total number of items: 48