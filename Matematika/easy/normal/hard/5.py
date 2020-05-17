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
    print ("1ton + 5kw + 10kg + 15hg + 20dag + 25g + 30dg + 35cg + 40mg =______kg").format(r,w)
    print ""
    select = input("jawaban: ")
    filtering(select)



def filtering(pilih):
    if pilih == 1511.72839:
        print ("anda benar")
        print ("lanjut ke profesional")
    else:
        print (r+"salah coba lagi"+w)
        os.sys.exit()

if __name__ == '__main__':
    main()