# 프록시 패턴: 객체에 접근하기 전에 가로채서 필터링/제어하는 패턴

# 실제 서버
class Server:
    def handle_request(self, ip):
        print(f'{ip} 요청 처리 완료')

# 프록시 (서버 앞에서 요청 가로채는 역할)
class ProxyServer:
    def __init__(self):
        # 메모리에 할당된 프록시서버 객체 안에 실제 서버 객체(정보)를 저장해둠
        self.server = Server()
        self.blocked_ips = ['666.666.666']  # 차단할 IP 목록

    def check_request(self, ip):
        if ip in self.blocked_ips:  # 금지 목록에 있으면 여기서 끊음
            print(f'{ip} 차단됨')
            return  # 여기서 함수 종료 → 아래 서버 호출까지 안 감
        self.server.handle_request(ip)  # 통과하면 실제 서버한테 요청 넘김

proxy = ProxyServer()
proxy.check_request('666.666.666')