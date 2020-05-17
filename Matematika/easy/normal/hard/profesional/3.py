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
    print ("3 akun youtube mendapatkan subscriber. akun A mendapatkan 168373 subscriber. akun B mendapatkan 199221 subscriber. dan akun C mendapatkan 199999 subscriber. pernyataan yang berikut adalah").format(r,w)
    print ("1. selisih subscriber B dan A adalah 111111 subscriber ")
    print ("2. selisih subscriber C dan B adalah 123456 subscriber")
    print ("3. ketiga akun tersebut subscriber nya dijumlahkan menjadi 567593")
    print ("4. ketiga akun tersebut subscriber nya dijumlahkan menjadi 667593")
    print ""
    select = input("jawaban: ")
    filtering(select)



def filtering(pilih):
    if pilih == 3:
        print ("anda benar")
        os.system('python2 4.py')
    else:
        print (r+"salah coba lagi"+w)
        os.sys.exit()

if __name__ == '__main__':
    main()