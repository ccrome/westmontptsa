from wp_keys import *

# wp_keys.py should included the following:
# consumer_key    = "ck_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"
# consumer_secret = "cs_xxxxxxxxxxxxxxxxxxxxxxxxxxxx"


#import oauthlib.oauth1
#
#
#client = oauthlib.oauth1.Client(consumer_key, client_secret=consumer_secret)
#uri, headers, body = client.sign(root_url)
#
#
#client = oauthlib.oauth1.Client(consumer_key, client_secret=consumer_secret,
#                                resource_owner_key)
#
#
#print uri
#print headers
#print body

root_url = "http://westmontptsa.org/wp"
from woocommerce import API

wcapi = API (url=root_url,
             consumer_key = consumer_key,
             consumer_secret = consumer_secret)
#products = wcapi.get("products")
#print products.json()
orders = wcapi.get("orders?filter[meta]=true")
import pprint

all_orders = orders.json()["orders"]
pp = pprint.PrettyPrinter(indent=4)
for order in all_orders:
    #print order.keys()
    try:
        meta = order["order_meta"]
        #u'Payer PayPal address'
        #u'Payment type'
        student_id = meta[u'Student ID']
        student_name = meta[u'Student Name']
        t_shirt = meta[u'T-Shirt Size']
        phone = order["customer"]["billing_address"]["phone"]
        parent_email = order["customer"]["billing_address"]["email"]
        completed_date = order[u'completed_at']
        for item in order["line_items"]:
            if item["name"] == u'Grad Night':
                parent_name = meta[u'Payer first name'] + " " + meta[u'Payer last name']
                student_dob = meta[u'Student Date Of Birth']
                student_email = meta[u'Student Email']
                print completed_date, student_name, student_dob, student_id, parent_name, phone, student_email, parent_email, t_shirt
    except KeyError:
        pass
