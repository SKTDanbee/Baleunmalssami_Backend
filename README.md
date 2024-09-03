# 바른말싸미 앱서비스 (backEnd)
## 시스템 아키텍쳐
![바른말싸미 아키텍처](https://github.com/user-attachments/assets/df64ade0-5d76-4cf1-be00-1e27c55f3884)
## ERD <img width="606" alt="image" src="https://github.com/user-attachments/assets/78573b27-f9bd-4c96-b30d-02be58a8ff89">

키패드를 통해 입력된 정보들은 text테이블에 저장되고, 리포트 생성API를 거쳐서 report테이블에 저장됩니다.

리포트 유형(report_type)은 다음과 같습니다.
  1. 부모용 리포트
  2. 자녀용 리포트
  3. 사이버폭력 리포트
유저 별로 리포트의 구분을 위해 report테이블은 report_date, child_id, report_type을 다중 PK로 설정 하였습니다. 
