import socket
from threading import *
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO
import requests
import socket

def send_info_to_elastic():
    host = socket.gethostname()
    port = 8000                 # The same port as used by the server
    r = requests.get("http://www.tsetmc.ir/Loader.aspx?ParTree=15")
    soup = BeautifulSoup(r.text, "html.parser")
    rows = soup.find("div", {"class": "box1 white tbl z4_4 h210"}).find("table", {"class": "table1"}).find("tbody").find_all("tr")

    for row in rows:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        cells = row.find_all("td")
        namad = '"'+cells[0].get_text()+'"'
        last_price = '"'+cells[1].get_text()+'"'
        last_deal = '"'+cells[3].get_text()+'"'
        lowest_price = '"'+cells[5].get_text()+'"'
        highest_price = '"'+cells[6].get_text()+'"'
        quantity = '"'+cells[7].get_text()+'"'
        volume = '"'+cells[8].get_text()+'"'
        value = '"'+cells[9].get_text()+'"'
        full_text="{namad:"+namad+",last_price:"+last_price+",last_deal:"+last_deal+",lowest_price:"+lowest_price+",highest_price:"+highest_price+\
                  ",quantity:"+quantity+",volume:"+volume+",value:"+value+"}"
        print(full_text)
        s.sendall(bytes(full_text, 'utf-8'))
        s.close()


send_info_to_elastic()
"""
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost"
port = 8000
print (host)
print (port)
#serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(8000).decode())
            self.sock.send(b'Oi you sent something to me')

serversocket.listen(5)

r = requests.get("http://www.tsetmc.ir/Loader.aspx?ParTree=15")

soup = BeautifulSoup(r.text, "html.parser")

rows = soup.find("div", {"class": "box1 white tbl z4_4 h210"}).find("table", {"class": "table1"}).find("tbody").find_all("tr")

for row in rows:
    #try:
        cells = row.find_all("td")
        namad = cells[0].get_text()
        last_price = cells[1].get_text()
        last_deal = cells[3].get_text()
        lowest_price = cells[5].get_text()
        highest_price = cells[6].get_text()
        quantity = cells[7].get_text()
        volume = cells[8].get_text()
        value = cells[9].get_text()
        #print("{namad: {} ,last_price: {} ,last_deal: {} ,lowest_price: {} ,highest_price: {} ,quantity: {} ,volume: {} ,value: {} }").format(namad,last_price,last_deal,lowest_price,highest_price,quantity,volume,value)
        print(namad)
    #except:
    #    print("An exception occurred")

while 1:
    clientsocket, address = serversocket.accept()
    client(clientsocket, address)
"""