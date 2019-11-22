# A wab scraper project
import requests
import smtplib
from bs4 import BeautifulSoup
from twilio.rest import Client

URL ='https://www.amazon.in/Corsair-Vengeance-2400MHz-Chipset-CMK8GX4M1A2400C16R/dp/B01ARHCZYO/ref=sr_1_2?keywords=ram&qid=1574424140&sr=8-2'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'}


# this function is responsible for sending the mail

def send_mail():
		server = smtplib.SMTP('smtp.gmail.com','587')
		server.ehlo()
		server.starttls()
		server.ehlo()

		server.login('souravraveendran6@gmail.com','ldcrwhqbiidngurw')

		subject = 'price fell'
		body = 'check the amazon link https://www.amazon.in/Corsair-Vengeance-2400MHz-Chipset-CMK8GX4M1A2400C16R/dp/B01ARHCZYO/ref=sr_1_2?keywords=ram&qid=1574424140&sr=8-2'

		msg = f'subject:{subject}\n\n{body}'
		server.sendmail(
				'souravraveendran6@gmail.com',
				'souravraveendran6@outlook.com',
				msg
			)
		print('email has been sent')
		print('message has been sent')
		server.quit()

# this function is responsible for sending the message

def send_sms():
	subject = 'price fell'
	body = 'check the amazon link https://www.amazon.in/Corsair-Vengeance-2400MHz-Chipset-CMK8GX4M1A2400C16R/dp/B01ARHCZYO/ref=sr_1_2?keywords=ram&qid=1574424140&sr=8-2'
	client = Client('AC1fae1febf0737f1e7aff62e4c7038b89','5af491750b91a756c19d2e442c4ae301')
	client.messages.create(to='+919567611892',
						from_ ='+13609723252',
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

	if (converted_price < 2500):
		send_mail()
		send_sms()

check_price()

