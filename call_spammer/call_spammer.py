import requests
#import os
from twilio.rest import Client
#from playsound import playsound

# def  music():
# 	os.system('start/MIN vlc "C:\\Users\\SOURAV R S\\Documents\\proj\\Pacific Rim OST Soundtrack - 01 -  MAIN THEME by Ramin Djawadi.mp3" --new-window/min')
def call_spam():
	
	acc_sid = 'ACC_ID'
	auth_token = 'AUTH_TOKEN'

	client = Client(acc_sid,auth_token)
	client.calls.create( url='https://ia800105.us.archive.org/5/items/PacificRimOSTSoundtrack01MAINTHEMEByRaminDjawadi/Pacific%20Rim%20OST%20Soundtrack%20-%2001%20-%20%20MAIN%20THEME%20by%20Ramin%20Djawadi.mp3',
						to ='number',
	 					from_ = 'number')

# music()

 while True:

	if __name__ == '__main__':
		print('spamming......')
		call_spam()
