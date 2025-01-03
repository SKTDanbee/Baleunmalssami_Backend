# 바른말싸미 앱서비스 (backEnd)
# 시스템 아키텍쳐
![바른말싸미 아키텍처](https://github.com/user-attachments/assets/df64ade0-5d76-4cf1-be00-1e27c55f3884)
# ERD 
<img width="606" alt="image" src="https://github.com/user-attachments/assets/78573b27-f9bd-4c96-b30d-02be58a8ff89">


---

## 주요 기능

### 1. **레포트 생성**  
- Text 테이블에 저장된 문장 데이터를 바탕으로 Report 테이블에 레포트를 생성.

### 2. **친구 간 비속어 랭킹 조회**  
- Text 테이블의 데이터를 분석하여 친구 간 비속어 사용량을 비교, 순위화.

### 3. **부모-자녀 간 연동**  
- 자녀 계정과 부모 계정을 연동하여, 부모가 자녀의 활동을 확인할 수 있도록 구현.  
- 연동은 자녀가 입력한 부모의 휴대폰 번호와 부모 ID를 기반으로 이루어짐.
- 자녀가 회원가입하면 입력된 부모 휴대전화 번호로 SMS 인증번호가 전송된다. 이 때 SMS 전송은 coolSMS API를 사용하며 인증번호는 랜덤난수로 생성하여 발송한다.
