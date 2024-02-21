def n_for_m_offer(items, sku, sku_count, offer):
    # Check that offer is possible
    if sku_count < offer["count"]:
        return 0
    value = (sku_count // offer["count"]) * offer["price"]
    items[sku] -= offer["count"] * (sku_count // offer["count"])
    return value


def x_for_y_offer(items, sku, sku_count, offer):
    # Check if the free item exists in the basket
    if offer["offer_sku"] not in items:
        return 0
    # Check if there is enough x for the offer and there is enough y to offer
    if sku_count < offer["count"] or items[offer["offer_sku"]] < offer["offer_count"]:
        return 0
    # Remove the free items from the basket
    items[offer["offer_sku"]] -= (sku_count // offer["count"]) * offer["offer_count"]
    if items[offer["offer_sku"]] < 0:
        items[offer["offer_sku"]] = 0
    # X items will be charged individually at the end
    return 0


def BOGOF_offer(items, sku, sku_count, offer):
    # check if the offer is possible
    if sku_count < offer["count"]:
        return 0
    # Apply the offer by removing the free items from the basket
    items[sku] -= (sku_count // offer["count"]) * offer["offer_count"]
    if items[sku] < 0:
        items[sku] = 0
    return 0


def n_in_items_offer(items, bundle_items: set[str], bundle_size, bundle_price):
    # Check if at least bundle_size amount of items is in the basket
    if sum([list(items.keys()).count(item) for item in bundle_items]) < bundle_size:
        return 0

    bundles_basket = {(item, items[item]) for item in bundle_items if item in items and items[item] > 0}
    # Sort by price and remove the most expensive items
    bundles_basket = dict(sorted(bundles_basket, key=lambda x: x[1], reverse=True))
    bundle_basket_size = sum(list(bundles_basket.values()))
    value = (bundle_basket_size // bundle_size) * bundle_price

    for item, count in bundles_basket.items():
        if bundle_basket_size <= 0:
            break

        if count > bundle_basket_size:
            items[item] -= bundle_basket_size
            break

        bundle_basket_size -= count
        del items[item]

    return value



