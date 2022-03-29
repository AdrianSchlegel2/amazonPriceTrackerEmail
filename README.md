# amazonPriceTrackerEmail
A program that tracks the price of an amazon article. I used the requests and bs4 module to get the data of the price. *(You can replace the link with any product you want to track)*. Then I entered a max price at which I would be ready to buy the article. Then an if statement checked the real price against my max price and sends me an email per the smtplib module when it checks out. *(Just enter your email, password and the to email)*.

To have the full effectivity of the program you should automize it by letting it run daily on a server or a webhosting servicy like pythonAnywhere.
