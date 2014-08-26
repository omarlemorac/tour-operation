# -*- coding: utf-8 -*-
{
    "name":"Tour Operation",
    "description":"""\
Tour Operation functionality
_____________________________________________

- Manage tour products:
  Cruises, accommodations, flight tickets, lodges, transfers, miscellaneous.
- Travel itinerary. TODO:
- Manage pax (passengers). TODO:
- Invoice creation. TODO:
- Account invoice integration. TODO:
    """,
    "category":"Tour & Travel Operation",
    "author":"Accioma",
    "data":["security/res_groups.xml",
            "security/ir.model.access.csv",
            "views/tourproduct_view.xml",
            "views/tourcategories_view.xml",
            "views/product_product_view.xml",
           ],

    "depends":["base", "sale", "crm"],
    "installable":True
}
