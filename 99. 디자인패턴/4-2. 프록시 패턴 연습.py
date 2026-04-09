# 프록시 패턴
# 실제 서버로 들어가기 전에 요청을 가로채 필요한 작업을 수행

class Server:
    def receive_request(self, ip):
        print(f'{ip} 요청 수신 완료')

class ProxyServer:
    # 객체가 할당된 메모리의 초기값 세팅
    def __init__(self):
        self.server = Server()
        self.blocked_ips = ['666.666.666']
    
    def check_request(self, ip):
        if ip in self.blocked_ips:
            print(f'{ip} 요청 차단')
            return
        self.server.receive_request(ip)

proxy = ProxyServer()
proxy.check_request('666.666.666')