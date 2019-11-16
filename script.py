import requests

r = requests.get("https://bowentherapy.no")
print(r.status_code)
print(r.ok)
