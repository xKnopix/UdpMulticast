import socket
import struct


class UdpReciver():

    def __init__(self, group='224.1.1.1', port=5004):
        MCAST_GRP = group #'224.1.1.1'
        MCAST_PORT = port # 5004
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(('', MCAST_PORT))
        mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
        self.sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

    def recive(self, buffersize):
        return self.sock.recv(buffersize)