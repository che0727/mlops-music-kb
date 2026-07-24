# 🎵 Music Recommendation System  
개인 음악 데이터 기반 AI 추천 시스템

---

## 📌 프로젝트 소개

**Music Recommendation System**은  
사용자가 직접 음악 데이터를 기록하고 관리하며,  
AI를 통해 취향을 분석하고 새로운 음악을 추천받을 수 있는  
**개인 맞춤형 음악 데이터베이스 시스템**입니다.

기존 음악 추천 서비스와 달리  
플랫폼 데이터가 아닌 **사용자의 주관적 경험 데이터**를 기반으로  
추천과 분석이 이루어지는 것이 핵심 차별점입니다.

---

## 🎯 프로젝트 목표

- 개인의 음악 취향을 **데이터로 축적 및 구조화**
- LLM을 활용하여 **입력 부담 감소 및 데이터 확장**
- 축적된 데이터를 기반으로 **취향 분석 및 추천 제공**
- 간단하지만 **안정적이고 확장 가능한 MLOps 구조 설계**

---

## 🧠 핵심 아이디어

> "데이터를 쌓을수록 더 똑똑해지는 개인 음악 기록 시스템"

- 단순 추천 서비스 ❌  
- 개인 경험 기반 음악 아카이빙 + AI 분석 ✅  

---

## 🏗️ 시스템 아키텍처

Frontend (Streamlit)
↓
FastAPI (Backend API Server)
↓
Pandas (Data Processing)
↓
CSV Database (User-based storage)
↓
LLM API (Tag / Analysis / Recommendation)

--- 

## ⚙️ 기술 스택
 - **Language**: Python 3.14
 - **Frontend**: Streamlit
 - **Backend**: FastAPI
 - **Data Processing**: Pandas
 - **Database**: CSV 기반 파일 저장
 - **AI**: OpenAI API (LLM)
 - **Deployment**: Render
 - **Server**: Uvicorn
 - **Environment**: .env / python-dotenv

---

## 📂 프로젝트 구조
MLOps 프로젝트

├── app
│ └── main.py # Streamlit UI
│
├── api
│ ├── main.py # FastAPI 서버
│ ├── analysis.py # 데이터 분석 로직
│ ├── data_loader.py # CSV 입출력
│ └── llm.py # LLM API 호출
│
├── data
│ └── *.csv # 사용자별 데이터 저장

--- 
## 🚀 주요 기능 
### 1. 음악 데이터 등록
사용자가 직접 음악 정보를 입력하여 개인 음악 데이터베이스를 구축할 수 있습니다.

**저장 항목** 
- 제목 / 아티스트 / 국가 / 발매년도 
- 태그 / 사용자 메모 ✅ 특징 - 개인 감상 기반 데이터 저장 - 사용자별 데이터 분리 
- CSV 기반 경량 구조 
--- 
### 2. AI 태그 추천 입력된 음악 정보를 기반으로 AI가 자동으로 태그를 추천합니다. 
**입력** 
- 제목, 아티스트, 메모 
**출력 예시**
90년대 K-pop, 댄스 팝, 레트로, 사랑

  <img width="738" height="1300" alt="image" src="https://github.com/user-attachments/assets/86f34ae0-cc09-4421-b362-25e6cb0e10a6" />

<img width="814" height="584" alt="KakaoTalk_20260723_202659171_03" src="https://github.com/user-attachments/assets/c5b78f6b-5ac2-48a4-8ee0-97e734ed9024" />
<img width="600" height="215" alt="image" src="https://github.com/user-attachments/assets/a7bc194c-86a6-40ca-a50f-b4beaf6c0be5" />

✅ 효과 - 입력 부담 감소 - 데이터 구조화 - 음악 특징 확장 📸 (태그 추천 결과 스크린샷
 --- 
 ### 3. 음악 데이터 분석 누적 데이터를 기반으로 사용자의 취향을 분석합니다. 
 **분석 항목**
  - 국가별 분포
 - 아티스트 선호도
 - 주요 태그
 - 발매 시기 
 
 ✅ 특징 
 - 자연어 기반 분석 결과 제공 
 - 취향 해설 포함 
 
 ✅ 조건 
 - 최소 3곡 이상 데이터 필요 📸

![Uploading KakaoTalk_20260723_202659171_03.png…]()

  --- 
  ### 4. AI 음악 추천 사용자의 데이터를 기반으로 맞춤형 음악을 추천합니다. 
  - 추천 개수: 3~5곡 
  - 포함 내용: - 추천 이유 
  - 간단한 설명 
  
 ✅ 특징 
  - 개인화 추천 
  - 설명 가능한 추천 📸
<img width="814" height="747" alt="KakaoTalk_20260723_202659171_02" src="https://github.com/user-attachments/assets/9f3f3036-b597-4606-955c-7c032d07d6d1" />

   --- 

## ❗예외처리
<img width="1437" height="1206" alt="예외처리" src="https://github.com/user-attachments/assets/3c4bf5b0-c2c9-4a92-af0a-8f6143a08c15" />
<img width="723" height="915" alt="예외처리  발매년도, 메모, 태그 비움 - 정상 저장" src="https://github.com/user-attachments/assets/60c905b3-4b94-4112-9ef1-66fef1224ecf" />
<img width="727" height="854" alt="예외처리  제목 비움-경고" src="https://github.com/user-attachments/assets/306ca4d0-f239-4d46-94da-2fa887aa79ca" />
<img width="729" height="854" alt="예외처리  아티스트 비움 - 경고" src="https://github.com/user-attachments/assets/54b3d7fe-b507-4f35-81a7-7021e778d146" />
<img width="743" height="145" alt="image" src="https://github.com/user-attachments/assets/17e0cdbc-5b97-4f23-aba1-adf331665806" />

   
## 💡 설계 철학 (차별성)
### 1. 개인 경험 중심 데이터
플랫폼 데이터가 아닌 사용자의 감상과 경험 기반 데이터 활용
 --- 
### 2. 단순하지만 안정적인 구조
 - CSV 기반 설계 
 - 명확한 데이터 흐름 
 --- 
 ### 3. 신뢰도 중심 설계 
 - 최소 데이터 조건 (3곡 이상) 
 - 입력 검증 및 예외 처리
  --- 
  ## 🛡️ 안정성 및 예외 처리
   - API 연결 실패 처리
   - Timeout 예외 처리 
   - 사용자 입력 검증 
   - 데이터 부족 시 기능 제한 
   - CSV 파일 자동 생성 
   - Null 값 처리 👉 "기능"보다 "안정성"에 집중 
   --- 
   ## ⚠️ 한계점 
   ### 1. 추천 정확도 
   - 기존 곡 완전 필터링 어려움 
   - LLM 의존도 높음 
   ### 2. 데이터 저장 구조 
   - CSV 기반 → 확장성 제한 
   ### 3. LLM 출력 
   - 비정형 문자열 → 후처리 어려움 
   --- 
   ## 🔧 향후 개선 방향 
   - 벡터 DB 기반 추천 시스템 도입 
   - JSON structured output 적용 
   - SQLite / NoSQL DB 전환 
   - 태그 정규화 시스템 구축 - 사용자 인증 기능 추가 
   --- 
   ## 📈 활용 가능성 
   - 개인 음악 아카이빙 서비스 
   - 음악 큐레이션 플랫폼 
   - 콘텐츠 추천 시스템 확장 
   - LLM 기반 개인화 서비스 모델 
   --- 
   ## ✅ 기대 효과 
   - 개인 취향 데이터 축적 
   - 데이터 기반 자기 이해 
   - 개인화 추천 정확도 향상 
   - 확장 가능한 서비스 구조 확보 
   --- 
   ## 🧑‍💻 개발 회고 
   본 프로젝트는 복잡한 기술보다는 **안정적으로 동작하는 시스템 구현**에 집중했습니다. 
   - 예외 처리 중심 설계 
   - 유지보수 가능한 구조 
   - 실제 서비스 확장 가능성 고려 
   👉 이를 통해 작은 기능이라도 "확실하게 동작"하도록 구현했습니다. 
   --- 
   ## 🔗 배포 링크 
   👉 https://mlops-music-kb-1.onrender.com 
   --- 
   ## 🙌 마무리
   이 프로젝트는 데이터, AI, 사용자 경험을 연결하는 개인화 추천 시스템의 기본 구조를 구현한 사례입니다. 앞으로 기능과 데이터를 확장하여 실제 서비스로 발전시키는 것을 목표로 합니다.
