import socket 

def run(domain):
    open_ports=[]
    ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 3306, 8080]
    for port in ports:
        try:
            with socket.socket(socket.AF_INET ,socket.SOCK_STREAM)as s:
                 s.settimeout(1)
                 if s.connect_ex((domain,port))==0:
                    open_ports.append(port)
        except:
            continue
    return open_ports
               
