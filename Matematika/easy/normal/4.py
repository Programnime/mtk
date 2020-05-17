#Jangan ganti author , hargai creator cape loh buat nya

import requests,re,os

b="\033[0;34m"
g="\033[1;32m"
w="\033[1;37m"
r="\033[1;31m"
y="\033[1;33m"
cyan = "\033[0;36m"
lgray = "\033[0;37m"
dgray = "\033[1;30m"
ir = "\033[0;101m"
reset = "\033[0m"



def main():
    os.system('clear')
    print ("Matematika Soal USBN From Arytafa")
    print ("KPK dari 12, 15 dan 40 =").format(r,w)
    print ""
    select = input("jawaban: ")
    filtering(select)



def filtering(pilih):
    if pilih == 120:
        print ("anda benar")
        os.system('python2 5.py')
    else:
        print (r+"salah coba lagi"+w)
        os.sys.exit()

if __name__ == '__main__':
    main()