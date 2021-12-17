import socket

class Udpsender():

    def __init__(self, group='224.1.1.1', port=5004):
        self.group = group
        self.port = port
        ttl = 2  # ?
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, ttl)

    def send(self,bytebuffer):
        self.sock.sendto(bytebuffer, (self.group,self.port))