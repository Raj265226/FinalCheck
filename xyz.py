import requests

response = requests.get("http://216.10.245.166/Library/GetBook.php?AuthorName=Roh")

print(response.status_code)
print(response.text)