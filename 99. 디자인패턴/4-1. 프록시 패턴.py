# 프록시 패턴: 객체에 접근하기 전에 가로채서 필터링/제어하는 패턴

# --- 실제 서버 ---
class Server:
    def handle_request(self, ip):
        print(f"{ip} 요청 처리 완료")

# --- 프록시 (서버 앞에서 요청을 가로채는 역할) ---
class ProxyServer:
    def __init__(self):
        self.server = Server()  # 실제 서버를 내부에 갖고 있음
        self.blocked_ips = ["666.666.666.666"]  # 차단할 IP 목록

    def handle_request(self, ip):
        if ip in self.blocked_ips:  # 차단 대상이면 막음
            print(f"{ip} 차단됨!")
            return
        self.server.handle_request(ip)  # 통과하면 실제 서버로 넘김

# --- 사용 ---
proxy = ProxyServer()
proxy.handle_request("123.456.789.0")    # 123.456.789.0 요청 처리 완료
proxy.handle_request("666.666.666.666")  # 666.666.666.666 차단됨!