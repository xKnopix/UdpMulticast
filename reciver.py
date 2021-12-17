from networking.reciver import UdpReciver
from data.parsedatastructure import Parsedata

reciver = UdpReciver()

while True:
    data = reciver.recive(1024)
    print(data)
    pdata = Parsedata.parse(data)
    print(pdata)