import requests
from time import time

time_ini=time()

barcode='insert barcode here'

url_barcode='https://api.bsale.cl/v1/price_lists/23/details.json?barcode='+barcode
token= 'insert your token here'

head= {'Content-Type':'application/json','access_token':token}

r=requests.get(url_barcode,headers=head)
r=r.json()
print(r)
price = r['items'][0]['variantValueWithTaxes']

print (price)

time_end=time()
time_total=time_end-time_ini

print  (time_total, "segundos")