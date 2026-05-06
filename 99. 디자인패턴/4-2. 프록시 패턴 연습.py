# 프록시 패턴
# 클라이언트에서 서버로 가는 요청을 가로채서 필요한 작업(해킹 파악 등) 가능

class Server:
    def handle_request(self, ip):
        print(f'{ip}로부터 온 요청 처리')

class ProxyServer:
    # 초기값 세팅
    def __init__(self):
        self.server = Server()
        self.blocked_ips = ['666.666.666']
    
    def handle_request(self, ip):
        if ip in self.blocked_ips:
            print(f'{ip}로부터 온 요청 차단')
            return
        self.server.handle_request(ip)

proxy = ProxyServer()
proxy.handle_request("123.456.789.0")    
proxy.handle_request("666.666.666") 