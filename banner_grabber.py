import socket
import ssl

def run(domain, ports):
    banners = {}
    for port in ports:
        try:
            with socket.create_connection((domain, port), timeout=3) as sock:
                if port == 443:
                    context = ssl.create_default_context()
                    with context.wrap_socket(sock, server_hostname=domain) as ssock:
                        ssock.send(b"HEAD / HTTP/1.1\r\nHost: " + domain.encode() + b"\r\n\r\n")
                        banners[port] = ssock.recv(1024).decode(errors='ignore')
                else:
                    sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                    banners[port] = sock.recv(1024).decode(errors='ignore')
        except Exception as e:
            banners[port] = f"No banner or error: {e}"
    return banners
