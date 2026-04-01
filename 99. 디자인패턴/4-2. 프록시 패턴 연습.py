# 프록시 패턴
# 객체에 접근하기 전에 가로채서 필요한 작업을 수행

# 실제서버
class Server:
    def handle_request(self, ip):
        print(f'{ip} 요청 처리 완료')

# 프록시 서버
class ProxyServer:
    def __init__(self):
        self.server = Server() #내부에 서버 정보 갖고있음
        self.blocked_ips = ['666.666.666']
    
    def check_request(self, ip):
        if ip in self.blocked_ips: # 프록시 서버 내부에 저장되어있는 금지 IP로 인한 요청이면
            print(f'{ip} 요청 차단')
            return
        return self.server.handle_request(ip) # 아니면 요청 정상 처리

proxy = ProxyServer()
proxy.check_request('111.111.111')
proxy.check_request('666.666.666')