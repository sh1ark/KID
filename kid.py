#!/bin/python
###############
r="\33[31;1m" #
b="\33[34;1m" #
g="\33[32;1m" #
w="\33[33;0m" #
###############
##########################################
import requests,sys,os,time,getpass      #
##########################################
########################################
print ("Sh1ark is Changed To Me3dR !!") #
########################################

class main():
	def banner(self):
		print("""
                _.-'''-.
              ." \      `".
             /  .-"---._   \
            |_/  _   _ `\_ |
            / |  o   o  | \
            \/     7     \/
             \   .___.   /
              '._  _  _.'
		   	     )   (     
	----------------------------------
	|				 |
	|      Tool BY MeHdi [Me3dR]     |
	|				 |
	----------------------------------
		Press EnTer Please
		""")
		o=getpass.getpass(" ")
	def values(self):
		print("""
	Values
	-----------------------------------
	
	url    :  <e.g set url google.com>
	list   :  <you can choose default list By Typing <set list dt or you can choose a list By Typing set list example.txt or you can search for upload page by type set list up>
	
	-----------------------------------
	""")
	def help(self):
		print("""
	# -----------------------------------------
	# Hi Guys I Hope This Script Help You 
	# _________________________________________
	#   Author   :   MeHdi Boullouf [ Me3dR ]
	#   Script   :   The_Kid
	#   Lisence  :   GNU LISENCE
	#   Facebook :   fb.com/mehdiboullouf16
	#   Team     : 	 Algerian LulZSec
	#-------------------------------------------
		
	COMMANDS
	------------------------------
		
	   help        : Show Help Menu
	   set <value> : Set Values
	   show values : Show Values Menu
	   start       : Start Searching
		
	------------------------------
	""")
	def cyborg(self,lista,url):
		o = open(lista,"r")
		er = o.readlines()
		if url.endswith("/"):
			path = url
		else:
			path = (url+"/")
		for my_bitch in er:
			req = requests.get(path+my_bitch)
			serf = req.text
			print("Try {}".format(path+my_bitch))
			if "<php" in serf:
				print("Fuck Iget Shell >{}".format(path+my_bitch))
			else:
				print("No Shell !")
	def work(self):
		global lista,url
		while True:
			cmdmehdi = input("Me3dR@LulZSeC    :")
			if cmdmehdi == "help":
				main().help()
			elif cmdmehdi == "show values":
				main().values()
			elif "set url" in cmdmehdi:
				url = cmdmehdi.split()[-1]
				print("URL > "+url)
			elif "set list" in cmdmehdi:
				lista = cmdmehdi.split()[-1]
				print("LIST > "+lista)
			elif "start" in cmdmehdi:
				if "dt" in lista:
					try:
						
						lista = "modules/default.txt"
						main().cyborg(lista,url)
					except NameError:
						print("Set Values And Try Again ! ")
				elif "txt" in lista:
					try:
						lista = lista
						main().cyborg(lista,url)
					except NameError:
						print("Set values and try again ! ")
				elif "up" in lista:
					try:
						lista = "modules/uploads.txt"
						main().cyborg(lista,url)
					except NameError:
						print("Set values and try again ! ")
					
			else:
				print("Are You Drink ?? [ Mttmnikch ]")
	
main().banner()
main().work()


# Hi Guys I Hope This Script Help You 
# _____________________________________
#	Author   :   MeHdi Boullouf [ Me3dR ]
#   Script   :   The_Kid
#   Lisence  :   GNU LISENCE
#   Facebook :   fb.com/mehdiboullouf16
#   Team     : 	 Algerian LulZSec
#-------------------------------------		