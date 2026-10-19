import urllib.request

res = urllib.request.urlopen('http://localhost:5173/')
html = res.read().decode('utf-8')
print("Server serving HTML length:", len(html))
print("Contains eyebrow class:", "eyebrow" in html)
print("Contains INTERCHANGEABLE TIPS:", "INTERCHANGEABLE TIPS" in html.upper())
print("Contains PRODUCT ANATOMY:", "PRODUCT ANATOMY" in html.upper())
