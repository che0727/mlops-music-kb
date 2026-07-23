# 🎵 Music Recommendation System

AI를 활용하여 사용자의 음악 데이터를 저장하고, 음악 취향을 분석하며, 맞춤형 음악을 추천하는 개인 음악 데이터베이스 프로젝트입니다.

---

# 📌 프로젝트 소개

Music Recommendation System은 사용자가 직접 음악 정보를 기록하고 관리할 수 있는 개인 음악 데이터베이스입니다.

사용자는 음악 정보를 입력하여 데이터를 저장할 수 있으며, 태그를 직접 입력하거나 AI에게 추천받을 수도 있습니다.

누적된 음악 데이터를 기반으로 사용자의 음악 취향을 분석하고, AI가 취향에 맞는 새로운 음악을 추천합니다.

---

# ✨ 주요 기능

### 🎵 음악 데이터 저장

* 음악 제목 입력
* 아티스트 입력
* 국가 선택
* 보컬 유형 선택
* 발매년도 입력
* 메모 작성
* 태그 직접 입력
* CSV 데이터베이스 저장

---

### 🏷️ AI 태그 추천

입력한 음악 정보를 기반으로 LLM(OpenAI API)이 적절한 태그를 추천합니다.

예시

```
K-pop, Summer, Female Vocal, Dance Pop, Bright
```

---

### 📊 음악 취향 분석

저장된 CSV 데이터를 분석하여

* 선호 국가
* 선호 보컬
* 많이 들은 아티스트
* 많이 사용한 태그
* 발매년도 분포

등을 AI가 자연어로 분석하여 제공합니다.

---

### 🎧 음악 추천

누적된 음악 데이터를 기반으로

사용자의 취향에 맞는 음악을 AI가 추천합니다.

추천 결과에는 추천 이유도 함께 제공합니다.

---

# 🛠 기술 스택

### Frontend

* Streamlit

### Backend

* FastAPI

### AI

* OpenAI API

### Data

* Pandas
* CSV

### Language

* Python

---

# 📁 프로젝트 구조

```
MLOps 프로젝트
│
├── app
│   └── main.py                 # Streamlit UI
│
├── api
│   ├── main.py                 # FastAPI
│   ├── analysis.py             # 데이터 분석
│   ├── data_loader.py          # CSV 입출력
│   └── llm.py                  # OpenAI 호출
│
├── data
│   └── music_archive.csv
│
├── .env
│
└── requirements.txt
```

---

# 🚀 실행 방법

## 1. 패키지 설치

```bash
pip install -r requirements.txt
```

---

## 2. FastAPI 실행

```bash
uvicorn api.main:app --reload
```

Swagger 문서

```
http://127.0.0.1:8000/docs
```

---

## 3. Streamlit 실행

```bash
streamlit run app/main.py
```

---

# 📷 프로그램 화면

(추후 스크린샷 추가)

* 메인 화면
* AI 태그 추천
* 음악 취향 분석
* 음악 추천 결과

---

# 🔄 시스템 흐름

```
사용자 입력

        │

        ▼

CSV 저장

        │

        ▼

데이터 분석

        │

        ▼

OpenAI API

        │

        ▼

AI 태그 추천
AI 취향 분석
AI 음악 추천

        │

        ▼

Streamlit 화면 출력
```

---

# 📅 개발 일정

| Day   | 내용                      |
| ----- | ----------------------- |
| Day 1 | 프로젝트 기획 및 환경 구축         |
| Day 2 | FastAPI 및 OpenAI API 연동 |
| Day 3 | Streamlit UI 구현 및 기능 연결 |
| Day 4 | 오류 처리, GitHub 정리 및 배포   |
| Day 5 | 프로젝트 발표                 |

---

# 👥 팀원

* 차하은

---

# 💡 향후 개선 사항

* 음악 앨범 이미지 표시
* Spotify API 연동
* 검색 기능
* 사용자 로그인
* 데이터 삭제 및 수정 기능
* 데이터 시각화 대시보드
* 추천 알고리즘 고도화
