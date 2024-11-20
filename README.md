# 바른말싸미 앱서비스 (backEnd)
## 시스템 아키텍쳐
![바른말싸미 아키텍처](https://github.com/user-attachments/assets/df64ade0-5d76-4cf1-be00-1e27c55f3884)
## ERD 
<img width="606" alt="image" src="https://github.com/user-attachments/assets/78573b27-f9bd-4c96-b30d-02be58a8ff89">
# 바른말싸미 ERD 설명

## 테이블 구성

### 1. **Child 테이블**  
- 자녀 계정 정보를 저장하는 엔티티.  
- **주요 필드**:  
  - 아이디 (ID)  
  - 비밀번호 (Password)  
  - 이름 (Name)  
  - 부모의 휴대폰 번호 (Parent Phone Number)  
  - 부모 아이디 (Parent ID)  

### 2. **Parent 테이블**  
- 부모 계정 정보를 저장하는 엔티티.  
- **주요 필드**:  
  - 아이디 (ID)  
  - 비밀번호 (Password)  
  - 이름 (Name)  
  - 부모 본인의 휴대폰 번호 (Phone Number)  

### 3. **Report 테이블**  
- 생성된 레포트 데이터를 저장하는 엔티티.  
- **주요 필드**:  
  - 레포트 생성 날짜 (Report Date)  
  - 자녀 ID (Child ID)  
  - 레포트 유형 (Report Type)  
  - 기타 레포트 관련 데이터  

### 4. **Text 테이블**  
- 입력된 문장 단위 데이터를 저장하는 엔티티.  
- **주요 필드**:  
  - 문장 내용 (Text Content)  
  - 자녀 ID (Child ID)  
  - 입력 시간 (Input Timestamp)  

### 5. **Friend 테이블**  
- 자녀의 친구 정보를 저장하는 엔티티.  
- **주요 필드**:  
  - 친구 ID (Friend ID)  
  - 자녀 ID (Child ID)  

---

## 주요 기능

### 1. **레포트 생성**  
- Text 테이블에 저장된 문장 데이터를 바탕으로 Report 테이블에 레포트를 생성.

### 2. **친구 간 비속어 랭킹 조회**  
- Text 테이블의 데이터를 분석하여 친구 간 비속어 사용량을 비교, 순위화.

### 3. **부모-자녀 간 연동**  
- 자녀 계정과 부모 계정을 연동하여, 부모가 자녀의 활동을 확인할 수 있도록 구현.  
- 연동은 자녀가 입력한 부모의 휴대폰 번호와 부모 ID를 기반으로 이루어짐.
