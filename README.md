# 바른말싸미 앱서비스 (backEnd)
## 시스템 아키텍쳐
![바른말싸미 아키텍처](https://github.com/user-attachments/assets/df64ade0-5d76-4cf1-be00-1e27c55f3884)
## ERD 
<img width="606" alt="image" src="https://github.com/user-attachments/assets/78573b27-f9bd-4c96-b30d-02be58a8ff89">
그림은 바른말싸미 ERD를 나타낸 것입니다.
- Child와 Parent 테이블은 각각 자녀와 부모의 계정 정보를 저장하는 엔티티로 공통적으로 아이디, 비밀번호, 이름을 포함한다. Child 테이블에는 부모의 휴대폰 번호와 부모 아이디가 추가로 저장되며, Parent 테이블에는 부모 본인의 휴대폰 번호가 저장된다.
- Report와 Text 테이블은 레포트 생성과 관련된 데이터를 저장한다. Report 테이블은 생성된 레포트를, Text 테이블은 입력된 문장 단위 데이터를 저장한다.
- Friend 테이블은 자녀의 친구 정보를 저장한다.

바른말싸미는 레포트 생성, 친구 간 비속어 랭킹 조회, 부모-자녀 간 연동의 기능을 제공한다. 이를 구현하기 위해 백엔드에 주요 엔드포인트를 설정하였다.
