# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    prices = {
        'A': {
            "price": 50,
            "offers": {
                "3": 130
            }
        },
        'B': {
            "price": 30,
            "offers": {
                "2": 45
            }
        },
        'C': {
            "price": 20,
            "offers": {}
        },
        'D': {
            "price": 15,
            "offers": {}
        }
    }
    # Get the list of items with a number per item
    items = {}
    items_list = list(skus)
    for item in items_list:
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

    basket_total = 0

    for item in items:
        if item not in prices:
            return -1
        
    raise NotImplementedError()


