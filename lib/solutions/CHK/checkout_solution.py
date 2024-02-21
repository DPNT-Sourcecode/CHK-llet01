# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str):
    prices = {
        'A': {
            "price": 50,
            "offers": {
                3: 130
            }
        },
        'B': {
            "price": 30,
            "offers": {
                2: 45
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

    for sku, sku_count in items.items():
        # SKU must be in the prices table
        if sku not in prices:
            return -1

        # No offers are possible if the count is less than the offer or no offers exist
        if prices[sku]["offers"] sku_count < prices[sku]["offers"].keys()[0]:
            basket_total += sku_count * prices[sku]["price"]

        # Find any offers and add to the basket total
        if sku_count in prices[sku]["offers"]:
            basket_total += prices[sku]["offers"][sku_count]
            continue


    return basket_total

