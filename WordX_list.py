# Tool Created By : T3rr8us
# Tool : Basic Wordlist Generator
# Version : WordX_list 2.0
# Team : CafSechax
# Thank You For Using This Tool Hope You Like It ;)

import itertools
import sys
import time

def Writertext(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.07)

def tik():
	titik = ['.   ','..  ','... ']
	for o in titik:
		print("\r\x1b[1;93mPlease Wait \x1b[1;93m"+o),;sys.stdout.flush();time.sleep(1)

back = 0
berhasil = []
cekpoint = []
oks = []
id = []
listgrup = []
vulnot = "\033[31mNot Vuln"
vuln = "\033[32mVuln"

# Banner
ban = '''
                                                    '''
print("\n")
Writertext("""\033[1;32;40m  ___________
 < WordX 2.0 >              
  ———————————
                            (*) Basic Wordlist
      \                     (*) User
   \033[1;31;40m    \   ,__,             (*) Passwords
        \  (oo)____         (*) Generator
           (__)    )  \
                                                   ||--|| *                                          Wordlist Generator     [*] By : T3rr8us P74NK                                     [*] Team : CafSecHax                                       \033[1;32;40m[*] Website : https://anonymous                             -pyr4mid.blogspot.com/?m=1""")

print("\n")
print(""" 
\033[1;31;40m —————————————————————————————————————————————————————————
 \033[1;32;40m[+]> \033[1;31;40mInsert the information about the victim to make a      dictionary.
 
 \033[1;32;40m[+]>\033[1;31;40m If you don't know all the info, just hit enter when asked! ;)!
 —————————————————————————————————————————————————————————""")
 
# User Inputs
print(" ")
print(" ")
scale = input('\033[1;32;40m[!!] provide a wordlist size [ex: 1 to 5 = 1 to 5] : ')
start = int(scale.split('to')[0])
final = int(scale.split('to')[1])

use_nouse = str(input("\n\033[1;32;40m[+] Do you want to enter personal data ? [y/N]: "))
if use_nouse == 'y':
	nick_name = str(input("\n\033[1;31;40m> Nick Name: "))
	first_name = str(input("\n\033[1;31;40m> Fist Name: "))
	last_name = str(input("\n\033[1;31;40m> Last Name: "))
	birthday = str(input("\n\033[1;31;40m> Birthday: "))
	month = str(input("\n\033[1;31;40m> Month: "))
	year = str(input("\n\033[1;31;40m> Year: "))
	print(" ")
	print(" ")
	part_name = str(input("\n\033[1;31;40m> Partner full Name: "))
	part_nickname = str(input("\n\033[1;31;40m> Partner NickName: "))
	part_birth = str(input("\n\033[1;31;40m> Partner full Birthday: "))
	print(" ")
	print(" ")
	child_name = str(input("\n\033[1;31;40m> Child's full Name: "))
	child_nickname = str(input("\n\033[1;31;40m> Child's NickName: "))
	child_birth = str(input("\n\033[1;31;40m> Child's full Birthday: "))
	print(" ")
	print(" ")
	cp_no = str(input("\n\033[1;31;40m> Target Cell Phone Number: "))
	company = str(input("\n\033[1;31;40m> Company Name: "))
	print(" ")
	print(" ")
	mother = str(input("\n\033[1;31;40m> Mother full Name: "))
	father = str(input("\n\033[1;31;40m> Father full Name: "))
	brother = str(input("\n\033[1;31;40m> Brother full Name: "))
	Sister = str(input("\n\033[1;31;40m> Sister full Name: "))

# Genn		
	chrs = nick_name + first_name + last_name + birthday + month + year + part_name + part_nickname + part_birth + child_name + child_nickname + child_birth + company + cp_no + mother + father + brother + Sister

		
else:
	chrs = 'abcdefghijklmnopqrstuvwxyz'
	pass


chrs_up = chrs.upper()
chrs_specials = '!\][/?.,~-=";:><@#$%&*()_+\' '
chrs_numerics = '1234567890'

# File Input
file_name = input('\n\033[1;32;40m[!!] Insert a name of your wordlist file: ')
arq = open(file_name, 'w')
if input('\n\033[1;32;40m[+] Do you want to use uppercase characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_up])
	
if input('\n\033[1;32;40m[+] Do you want to use special characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_specials])
	
if input('\n\033[1;32;40m[+] Do you want to use numeric characters? (y/n): ') == 'y':
	chrs = ''.join([chrs, chrs_numerics])


for i in range(start, final+1):
	for j in itertools.product(chrs, repeat=i):
		temp = ''.join(j)
		print(temp)
		arq.write(temp + '\n')
arq.close()