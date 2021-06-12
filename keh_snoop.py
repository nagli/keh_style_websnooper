import urllib3
from urllib.parse import quote_plus

https = urllib3.PoolManager()
# url = quote_plus('https://www.missguidedau.com/petite-black-msgd-insert-mesh-cut-out-gym-leggings-10202499')
# handler = https.urlopen('GET', 'https://api.proxycrawl.com/?token=A0hx10p8VV1qDTZsVFK08g&url=' + url)

url = quote_plus('https%3A%2F%2Fwww.amazon.com')
handler = https.urlopen('GET', 'https://api.proxycrawl.com/?token=wfvm8FppEqUn2T8nUa2W4w&url=' + url)


print(handler.data)
