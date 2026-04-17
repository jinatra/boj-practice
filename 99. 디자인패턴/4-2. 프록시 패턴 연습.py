# 프록시 패턴
# 서버로 요청이 넘어가기 전 가로채서 필요한 작업(해킹의심 등)을 수행

# 실제 서버
class Server:
    def handle_request(self, ip):
        print(f'{ip}로부터 들어온 요청 수행')

# 프록시 서버
class ProxyServer:
    def __init__(self):
        self.server = Server() #서버 정보를 들고있음
        self.blocked_ips = ['666.666.666', '999.999.999']
    
    def handle_request(self, ip):
        if ip in self.blocked_ips:
            print(f'{ip}로부터 들어온 요청 차단')
            return
        self.server.handle_request(ip)

# 테스트
proxy = ProxyServer()
proxy.handle_request('666.666.666')
proxy.handle_request('111.111.111')