def n_for_m_offer(items, sku, sku_count, offer):
    # Check that offer is possible
    if sku_count < offer.count:
        return 0
    value = (sku_count // offer.count) * offer.price
    items[sku] -= offer.count * (sku_count // offer.count)
    return value


def x_for_y_offer(items, sku, sku_count, offer):
    # Check if there is enough x for the offer and there is enough y to offer
    if sku_count < offer.count or items[offer.offer_sku] < offer.offer_count:
        return 0
    # Remove the free items from the basket
    items[offer.offer_sku] -= offer.offer_count
    # X items will be charged individually at the end
    return 0
