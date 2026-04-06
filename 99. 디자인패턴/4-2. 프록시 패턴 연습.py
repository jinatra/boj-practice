# 프록시 패턴
# 객체에 접근하기 전 가로채서 검증 등을 진행하는 패턴

# 실제 서버
class Server:
    def handle_request(self, ip):
        print(f'{ip}에서 온 요청 처리')

# 프록시 서버
class ProxyServer:
    def __init__(self):
        self.server = Server
        self.blocked_ips = ['666.666.666']
    
    def check_request(self, ip):
        if ip in self.blocked_ips:
            print(f'{ip}는 블록 IP라 접근 차단')
            return
        self.server.handle_request(ip)

p = ProxyServer()
p.check_request('666.666.666')