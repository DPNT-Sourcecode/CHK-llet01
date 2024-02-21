# noinspection PyUnusedLocal
# skus = unicode string
from .offer_helper_functions import *


def checkout(skus: str):
    if not isinstance(skus, str):
        return -1
    prices = {
        'A': {
            "price": 50,
            "offers": {
                3: {
                    "offer": n_for_m_offer,
                    "price": 130,
                    "priority": 1  # Doesn't matter atm
                },
                5: 200
            },
        },
        'B': {
            "price": 30,
            "offers": {
                2: {
                    "offer": n_for_m_offer,
                    "price": 45,
                    "priority": 2
                }
            }
        },
        'C': {
            "price": 20,
            "offers": {}
        },
        'D': {
            "price": 15,
            "offers": {}
        },
        'E': {
            "price": 40,
            "offers": {
                2: {
                    "offer": x_for_y_offer,
                    "price": 0,
                    "priority": 1,
                    "offer_sku": "B",
                    "offer_count": 1
                }
            }
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
    offer_queue: dict[int, list] = {}

    # Could iterate over the offers first, remove any items from skus that have been applied,
    # then add the individual charge at the end. The offers would be ordered to favor the customer. A offer is no applied
    # using a function that returns an updated sku and basket total. This would allow for a more dynamic offer system.
    # However, you shouldn't need to go through every offer even when the skus is only "A" or "B" for example.

    # Instead, find where all the offers that are available and put them in an ordered list based on priority. Then
    # execute the offers in order until no offers are found. Then add the individual items to the basket total.

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
            if prices[sku]["offers"][sku_count]["priority"] not in offer_queue:
                offer_queue[prices[sku]["offers"][sku_count]["priority"]] = []
            offer_queue[prices[sku]["offers"][sku_count]["priority"]].append(
                {"sku": sku, "count": sku_count, "offer": prices[sku]["offers"][sku_count]["offer"]})
            continue

        # Find the largest offer that is less than the count
        closest_smaller_offer_count = 0
        closest_smaller_price = 0
        for offer_count, offer_price in prices[sku]["offers"].items():
            if offer_count < sku_count:
                closest_smaller_offer_count = offer_count
                closest_smaller_price = offer_price
            if offer_count > sku_count:
                break

        offer_queue[prices[sku]["offers"][closest_smaller_offer_count]["priority"]].append(
            {"sku": sku, "count": sku_count, "offer": prices[sku]["offers"][closest_smaller_offer_count]["offer"]})

    # Execute the offers in order
    for priority in sorted(offer_queue.keys()):
        basket_total += sum(
            [offer["offer"](items, offer["sku"], offer["count"], offer["offer"]) for offer in offer_queue[priority]])

    # Add the individual items to the basket total
    for sku, sku_count in items.items():
        basket_total += sku_count * prices[sku]["price"]

    return basket_total

# for reference


# # No offers are possible if the count is less than the offer or no offers exist
# # Assuming offers are sorted in ascending order
# if not bool(prices[sku]["offers"]) or sku_count < list(prices[sku]["offers"].keys())[0]:
#     basket_total += sku_count * prices[sku]["price"]
#     continue

# # Find any 'perfect' offers and add to the basket total
# if sku_count in prices[sku]["offers"].keys():
#     basket_total += prices[sku]["offers"][sku_count]
#     continue
#
# # Find the largest offer that is less than the count
# closest_smaller_offer = 0
# closest_smaller_price = 0
# for offer_count, offer_price in prices[sku]["offers"].items():
#     if offer_count < sku_count:
#         closest_smaller_offer = offer_count
#         closest_smaller_price = offer_price
#     if offer_count > sku_count:
#         break
#
# # Add the left over individual items to the basket total
# basket_total += (sku_count % closest_smaller_offer) * prices[sku]["price"]
# # Add the offer to the basket total
# basket_total += (sku_count // closest_smaller_offer) * closest_smaller_price


# prices = {
#         'A': {
#             "price": 50,
#             "offers": {
#                 3: 130,
#                 5: 200
#             }
#         },
#         'B': {
#             "price": 30,
#             "offers": {
#                 2: 45
#             }
#         },
#         'C': {
#             "price": 20,
#             "offers": {}
#         },
#         'D': {
#             "price": 15,
#             "offers": {}
#         },
#         'E': {
#             "price": 40,
#             "offers": {
#                 # TODO: Implement this offer
#                 2: "get one B free"
#             }
#         }
#     }


