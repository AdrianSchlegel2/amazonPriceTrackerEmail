from bs4 import BeautifulSoup
import requests
import smtplib
import os

# Track the magic mouse price
URL = "Enter the URL of the article you want to track here"

# Enter your minimum price here \/
MINIMUM_PRICE = 0

LOGIN = os.environ["my_email"]
PASSWORD = os.environ["my_pass"]
TO_ADDRESS = os.environ["to_email"]

response = requests.get(URL, headers={
      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome"
      "/99.0.4844.83 Safari/537.36",
      "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
})
contents = response.text
soup = BeautifulSoup(contents, "html.parser")

price = soup.find(name="span", class_="a-offscreen").getText()
name = soup.find(name="span", id="productTitle").getText().strip()



# format price
formatted_price = price.replace("€", "")
formatted_price = float(formatted_price.replace(",", "."))

MESSAGE = f"Subject: Amazon Price Alert!\n\n{name} is now {price}.\n\n{URL}"
MESSAGE = MESSAGE.encode("utf-8")

if formatted_price <= MINIMUM_PRICE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=LOGIN, password=PASSWORD)
        connection.sendmail(from_addr=LOGIN, to_addrs=TO_ADDRESS, msg=MESSAGE)

else:
    print("The Price is not below the minimum price")
