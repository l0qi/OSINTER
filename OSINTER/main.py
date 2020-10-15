import requests as r
import urllib.request, json 
import core.menu as menu
import colorama
import core.user_agent as agent

menu.main()

choise = input('Enter select: ')

class Funct:
    def linkExtract(self):
        """ LINK EXTRACT """
        try:
            self.status = r.get('https://api.hackertarget.com/pagelinks/?q=' + url)
            for self.s in self.status:
                print(f'[Result]: {self.status.text}')

                with open('result/result.txt', 'w') as text_file:
                    text_file.write(str(self.status.text))
                    print(f'[+] Data saving!')
        except:
            print(f'You fuckin debil!')

    def subnet(self):
        """ SUBNET """
        try:
            self.sub = r.get('https://api.hackertarget.com/subnetcalc/?q=' + url)
            for self.s in self.sub:
                print(f'\n\033[33m[Result]: {self.sub.text}')

                with open('result/subnet.txt', 'w') as text_file:
                    text_file.write(str(self.sub.text))
                    print(f'[+] Data saving!')
        except:
            print(f'Infomation not found!')


    def subdom(self):
        """ SUBDOM """
        self.subdom = r.get('https://api.hackertarget.com/hostsearch/?q=' + url)
        for self.s in self.subdom:
            print(f'\n\033[33m[Result]: {self.subdom.text}')

            with open('result/subnet.txt', 'w') as text_file:
                text_file.write(str(self.subdom.text))
                print(f'[+] Data saving!')


    def phonesearch(self):
            """ PHONE SEARCH """
            try:
                self.result = urllib.request.urlopen(f'https://htmlweb.ru/geo/api.php?json&telcod={target}').read().decode('utf-8')
            except urllib.error.URLError:
                print('Something wrong!')

            try:
                self.result = json.loads(self.result)
                print(f'Страна: ' + self.result['country']['english']
                + '\nID: ' + self.result['country']['id']
                + '\nLocation: ' + self.result['country']['location']
                + '\nCity: ' + self.result['capital']['english']
                + '\nFullname: ' + self.result['country']['english'])
            except:
                print('Infomation not found!')


if choise == "1":
    url = input('\033[35m[URL]<-->: ')
    Funct.linkExtract(self = Funct())

elif choise == "2":
    url = input('\033[35m[IP/HOSTNAME]<-->:  ')
    Funct.subnet(self = Funct())

elif choise == "3":
    url = input('\033[35m[IP/HOSTNAME]<-->: ')
    Funct.subdom(self = Funct())

elif choise == "4":
    target = input('\033[35m[Phone]<-->: ')
    Funct.phonesearch(self = Funct())


else:
    print('\033[31mPermission is not the correct value')