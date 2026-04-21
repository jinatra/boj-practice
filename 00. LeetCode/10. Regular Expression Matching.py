class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # .: 아무 글자 하나와 매칭
        # *: 바로 앞 글자가 0번 이상 반복
        
        # 패턴이 비었으면 s도 비어야 True
        if not p:
            return not s
        
        # 첫 글자 매칭 확인
        first = len(s) > 0 and (s[0] == p[0] or p[0] == '.')
        
        # 여기서 *가 있는 경우 / 없는 경우로 나누기
        if len(p) >= 2 and p[1] == '*':
            # 선택 1: *를 0번 사용 -> 패턴 앞 두글자 건너뜀
            # 선택 2: *를 1번+ 사용 -> 첫 글자가 매칭되면 s만 한칸 진행
            return self.isMatch(s, p[2:] or (first and self.isMatch(s[1:], p)))
        else:
            return first and self.isMatch(s[1:], p[1:])