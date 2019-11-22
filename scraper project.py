# A wab scraper project
import requests
import smtplib
from bs4 import BeautifulSoup
from twilio.rest import Client

URL ='your urls'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


# this function is responsible for sending the mail

def send_mail():
		server = smtplib.SMTP('smtp.gmail.com','587')
		server.ehlo()
		server.starttls()
		server.ehlo()

		server.login('mail id','app password')

		subject = 'price fell'
		body = 'check the amazon link https://www.amazon.in/product link'

		msg = f'subject:{subject}\n\n{body}'
		server.sendmail(
				'mail ids',
				'mail ids',
				msg
			)
		print('email has been sent')
		print('message has been sent')
		server.quit()

# this function is responsible for sending the message

def send_sms():
	subject = 'price fell'
	body = 'check the amazon link https://www.amazon.in/product link'
	client = Client('acc_no','password')
	client.messages.create(to='number',
						from_ ='twilio number',
						body = f'subject:{subject}\n\n{body}' )

# This function looks up the products price in amazon

def check_price():

	page = requests.get(URL , headers=headers)
	soup = BeautifulSoup(page.content,'html.parser')
	title = soup.find(id = "productTitle").get_text()
	price = soup.find(id = "priceblock_ourprice").get_text()
	price = price.strip(',')
	price = price.replace(',','.')
	converted_price = float(price[1:7])
	converted_price = converted_price * 1000

	# print(soup.prettify())
	print(title.strip())
	print(price)
	print(converted_price)

	if (converted_price < 2500)#change the price:
		send_mail()
		send_sms()

check_price()

