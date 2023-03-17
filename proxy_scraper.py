import requests
from bs4 import BeautifulSoup

# Send a request to the URL and get the response
url = "https://free-proxy-list.net/"
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the proxy information
proxy_table = soup.find("table", attrs={"class": "table-bordered"})

# If table is found, iterate over its rows and get proxy information
if proxy_table is not None:
    with open("proxies.txt", "w") as file:
        for row in proxy_table.find_all("tr")[1:]:
            columns = row.find_all("td")
            ip = columns[0].get_text()
            port = columns[1].get_text()
            country_code = columns[2].get_text()
            anonymity = columns[4].get_text()
            https = columns[6].get_text()
            file.write(f"{ip}:{port}\n")
    print("Proxies written to proxies.txt")
else:
    print("Could not find proxy table on the page.")
