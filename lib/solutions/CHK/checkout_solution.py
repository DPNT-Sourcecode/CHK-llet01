# noinspection PyUnusedLocal
# skus = unicode string
from .offer_helper_functions import n_in_items_offer
from .prices_config import prices


def checkout(skus: str):
    if not isinstance(skus, str):
        return -1

    # Get the list of items with a number per item
    items: dict[str, int] = {}
    items_list = list(skus)
    for item in items_list:
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

    basket_total = 0
    offer_queue: dict[int, list] = {}

    # Apply bundle offers first
    basket_total = n_in_items_offer(items, ("Z", "S", "T", "Y", "X"), 3, 45)

    # Find all the offers that are available
    for sku, sku_count in items.items():
        # SKU must be in the prices table
        if sku not in prices:
            return -1

        # No offers are possible if the count is less than the offer or no offers exist
        # Assuming offers are sorted in ascending order
        if not bool(prices[sku]["offers"]) or sku_count < list(prices[sku]["offers"].keys())[0]:
            continue

        # Find any 'perfect' offers and add to the basket total
        if sku_count in prices[sku]["offers"].keys():
            if prices[sku]["offers"][sku_count]["priority"] not in offer_queue.keys():
                offer_queue[prices[sku]["offers"][sku_count]["priority"]] = []
            offer_queue[prices[sku]["offers"][sku_count]["priority"]].append(
                {"sku": sku, "count": sku_count, "offer": prices[sku]["offers"][sku_count]})
            continue

        # Find the largest offer that is less than the count
        for offer_count, offer_price in prices[sku]["offers"].items():
            if offer_count < sku_count:
                if prices[sku]["offers"][offer_count]["priority"] not in offer_queue.keys():
                    offer_queue[prices[sku]["offers"][offer_count]["priority"]] = []
                offer_queue[prices[sku]["offers"][offer_count]["priority"]].append(
                    {"sku": sku, "count": sku_count, "offer": prices[sku]["offers"][offer_count]})

    # Execute the offers in order
    for priority in sorted(offer_queue.keys()):
        basket_total += sum(
            [offer["offer"]["offer_function"](items, offer["sku"], items[offer["sku"]], offer["offer"]) for offer in
             offer_queue[priority]])

    # Add the individual items to the basket total
    for sku, sku_count in items.items():
        basket_total += sku_count * prices[sku]["price"]

    return basket_total


