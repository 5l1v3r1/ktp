# Author : ./FUKUR0-3XP
# Team : Black Coders Anonymous x AnonRoz Team
# Sorry Scriptnya Acak"an :'(

import os, re, time
try:
	import requests
except:
	os.system('pip2 install requests')
	os.system('python2 ' + __file__)
	
os.system('clear')
os.system('termux-setup-storage')
time.sleep(3)
if not os.path.exists('/storage/emulated/0/ktp'):
	os.mkdir('/storage/emulated/0/ktp')
else:
	pass
url = raw_input('Url KTP ( Index Of with http ): ')
print
print 'Proses Download'
a = 1
for x in re.findall(r'\<a\ href\=\"(.*?)\"\>', requests.get(url).text):
    if not '.jp' in x or not '.JP' in x:
        continue
    else:
        pass
    hm = requests.get(url + x)
    i = 1
    while os.path.exists('/storage/emulated/0/ktp/ktp%s.jpg' %i):
        i += 1
    am = open('/storage/emulated/0/ktp/ktp%s.jpg' %i,'wb').write(hm.content)

print
print 'Selesai'
print 'Liat Hasilnya Di Internal Kalian, Di Folder "ktp"'
