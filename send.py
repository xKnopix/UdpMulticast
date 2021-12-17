from networking.sencdr import Udpsender
from data.builddatastructure import Builddata

sender = Udpsender()

sdata = Builddata().build(1,2,3,4)

print(sdata)
# while True:
sender.send(sdata)