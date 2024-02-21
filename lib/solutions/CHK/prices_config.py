"""
This file contains the prices and offers for the checkout system.

The prices are stored in a dictionary with the SKU as the key and a dictionary as the value.
The value dictionary contains the price of the item and a dictionary of offers for the item.
Each offer is stored in a dictionary and can be configured with custom keys that are needed in the offer functions.
Each offer may have different priorities, the lower the priority the earlier the offer is applied.
"""
from .offer_helper_functions import *

prices = {
    'A': {
        "price": 50,
        "offers": {
            3: {
                "offer_function": n_for_m_offer,
                "price": 130,
                "count": 3,
                "priority": 2
            },
            5: {
                "offer_function": n_for_m_offer,
                "price": 200,
                "count": 5,
                "priority": 1
            }
        },
    },
    'B': {
        "price": 30,
        "offers": {
            2: {
                "offer_function": n_for_m_offer,
                "price": 45,
                "count": 2,
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
                "offer_function": x_for_y_offer,
                # "price": 0,
                "priority": 1,
                "count": 2,
                "offer_sku": "B",
                "offer_count": 1
            }
        }
    },
    'F': {
        "price": 10,
        "offers": {
            3: {
                "offer_function": BOGOF_offer,
                # "price": 20,
                "count": 3,
                "offer_count": 1,
                "priority": 1
            }
        }
    },
    'G': {"price": 20, "offers": {}},
    'H': {
        "price": 10,
        "offers": {
            5: {
                "offer_function": n_for_m_offer,
                "price": 45,
                "count": 5,
                "priority": 2
            },
            10: {
                "offer_function": n_for_m_offer,
                "price": 80,
                "count": 10,
                "priority": 1
            }
        }
    },
    'I': {"price": 35, "offers": {}},
    'J': {"price": 60, "offers": {}},
    'K': {
        "price": 70,
        "offers": {
            2: {
                "offer_function": n_for_m_offer,
                "price": 120,
                "count": 2,
                "priority": 1
            }
        }
    },
    'L': {"price": 90, "offers": {}},
    'M': {"price": 15, "offers": {}},
    'N': {
        "price": 40,
        "offers": {
            3: {
                "offer_function": x_for_y_offer,
                # "price": 120,
                "count": 3,
                "priority": 1,
                "offer_sku": "M",
                "offer_count": 1
            }
        }
    },
    'O': {"price": 10, "offers": {}},
    'P': {
        "price": 50,
        "offers": {
            5: {
                "offer_function": n_for_m_offer,
                "price": 200,
                "count": 5,
                "priority": 1
            }
        }
    },
    'Q': {
        "price": 30,
        "offers": {
            3: {
                "offer_function": n_for_m_offer,
                "price": 80,
                "count": 3,
                # Lower priority since 'R' offer is better value
                "priority": 2
            }
        }
    },
    'R': {"price": 50, "offers": {
        3: {
            "offer_function": x_for_y_offer,
            "count": 3,
            "priority": 1,
            "offer_sku": "Q",
            "offer_count": 1
        }
    }},
    'S': {"price": 20, "offers": {}},
    'T': {"price": 20, "offers": {}},
    'U': {
        "price": 40,
        "offers": {
            4: {
                "offer_function": BOGOF_offer,
                # "price": 120,
                "count": 4,
                "offer_count": 1,
                "priority": 1
            }
        }
    },
    'V': {
        "price": 50,
        "offers": {
            2: {
                "offer_function": n_for_m_offer,
                "price": 90,
                "count": 2,
                "priority": 2
            },
            3: {
                "offer_function": n_for_m_offer,
                "price": 130,
                "count": 3,
                "priority": 1
            }
        }
    },
    'W': {"price": 20, "offers": {}},
    'X': {"price": 17, "offers": {}},
    'Y': {"price": 20, "offers": {}},
    'Z': {"price": 21, "offers": {}}
}
