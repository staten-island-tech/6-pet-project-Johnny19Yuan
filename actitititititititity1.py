class hero:
    def __init__(self, name, money, inventory):
        self.name = name
        self.money = money
        self.inventory = inventory

    def buy(self, item):
        self.inventory.append(item)
        print(self.inventory)

Johnny = hero("Johnny",0.01,['One Band-Aid'])

Johnny.buy({"title": "Sheet of paper", "atk": 0.1})
