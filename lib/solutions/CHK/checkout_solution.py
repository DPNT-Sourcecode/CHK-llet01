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
        # Assuming offers are sorted in ascending order
        if not bool(prices[sku]["offers"]) or sku_count < prices[sku]["offers"].keys()[0]:
            basket_total += sku_count * prices[sku]["price"]
            continue

        # Find any 'perfect' offers and add to the basket total
        if sku_count in prices[sku]["offers"].keys():
            basket_total += prices[sku]["offers"][sku_count]
            continue

        # Find the largest offer that is less than the count
        closest_larger_offer = 0
        for offer_count, offer_price in prices[sku]["offers"].items():
            if offer_count > sku_count:
                basket_total += sku_count % offer_count * offer_price
                


    return basket_total


