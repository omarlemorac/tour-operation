# -*- coding: utf-8 -*-
{
    "name":"Tour Operation",
    "description":"""\
Tour Operator functionality
_____________________________________________

- Manage tour products:
  Cruises, acommodations, flight tickets, lodges, transfers, miscellaneous. TODO:
- Travel itinerary. TODO:
- Manage pax (passengers). TODO:
- Invoice creation. TODO:
- Account invoice integration. TODO:
    """,
    "category":"Tour & Travel",
    "author":"Accioma",
    "data":[  "views/tourproduct_view.xml"
            , "views/tourcategories_view.xml"
            , "views/product_product_view.xml"
           ],

    "depends":["base", "sale", "crm"],
    "installable":True
}
