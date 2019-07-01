import socket
import time
# 2 put the blind down, 1 put it up, 0 stop it


def shut_down():
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.connect(("192.168.0.35", 20000))
    SOCK.sendall("*2*2*21##".encode())
    SOCK.close()


def op_en():
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.connect(("192.168.0.35", 20000))
    SOCK.sendall("*2*1*21##".encode())
    SOCK.close()


def st_op():
    SOCK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SOCK.connect(("192.168.0.35", 20000))
    SOCK.sendall("*2*0*21##".encode())
    SOCK.close()


if __name__ == '__main__':
    #shut_down()
    #time.sleep(4)
    # st_op()
    #time.sleep(10)
    op_en()
