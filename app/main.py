import os
import streamlit as st
import requests

st.set_page_config(
    page_title="Music Recommendation",
    page_icon="🎵",
    layout="centered"
)

API_URL = os.getenv("API_URL", "http://127.0.0.1:8000")

# 시스템 안내
st.title("🎵 Music Recommendation System")
st.write("나만의 음악 데이터베이스를 만들고 AI 추천을 받아보세요.")
st.write("입력 데이터가 많아질 수록 더욱 정확한 맞춤 추천이 가능해집니다!")
st.caption("'*' 표시는 필수 입력 항목입니다.")

st.divider()

# 데이터 입력
st.subheader("👤 사용자")
username = st.text_input("닉네임을 입력하세요")

st.divider()

st.subheader("🎧 음악 정보 입력")
title = st.text_input("제목 *")
artist = st.text_input("아티스트 *")

country = st.selectbox(
    "국가 *",
    ["한국", "미국", "일본", "기타"]
)

vocal = st.selectbox(
    "보컬 *",
    ["남성", "여성", "혼성", "연주"]
)

since = st.text_input("발매년도 (선택)")
memo = st.text_area("메모 (선택)")

tags = st.text_input(
    "태그 (직접 입력 또는 AI 추천)(선택)",
    key="tags_input"
)



# AI 태그 추천 버튼
if st.button("🎵 AI 태그 추천"):

    if not title.strip():
        st.warning("제목을 입력해주세요.")
        st.stop()

    if not artist.strip():
        st.warning("아티스트를 입력해주세요.")
        st.stop()

    with st.spinner("AI가 태그를 추천하는 중입니다..."):
        data = {"title": title,
                "artist": artist,
                "memo": memo}
                
        try:
            response = requests.post(f"{API_URL}/recommend-tags", json=data, timeout=30)

        except requests.exceptions.ConnectionError:
            st.error("FastAPI 서버에 연결할 수 없습니다.")
            st.stop()

        except requests.exceptions.Timeout:
            st.error("응답 시간이 초과되었습니다.")
            st.stop()

    if response.status_code == 200:
        recommended_tags = response.json()["tags"]

        st.success("추천 완료!")
        st.markdown("### 🏷️ 추천 태그")
        st.info(recommended_tags)
        st.write("마음에 드는 태그를 입력하여 저장해 보세요!")

    else:
        st.error(f"추천 실패 ({response.status_code})")
        st.write(response.text)


# 데이터 저장 버튼
if st.button("💾 데이터 저장"):
    if not username.strip():
        st.warning("닉네임을 입력해주세요.")
        st.stop()

    if not title.strip():
        st.warning("제목을 입력해주세요.")
        st.stop()

    if not artist.strip():
        st.warning("아티스트를 입력해주세요.")
        st.stop()

    data = {
        "username": username,
        "title": title,
        "artist": artist,
        "country": country,
        "vocal": vocal,
        "since": since,
        "tags": tags,
        "memo": memo
    }
    
    try:
        response = requests.post(f"{API_URL}/add-music", json=data, timeout=30)

    except requests.exceptions.ConnectionError:
        st.error("FastAPI 서버에 연결할 수 없습니다.")
        st.stop()

    except requests.exceptions.Timeout:
        st.error("응답 시간이 초과되었습니다.")
        st.stop()

    if response.status_code == 200:
        st.success("저장 완료!")

        result = response.json()

        st.info(f"현재 저장된 음악 : {result['count']}곡")
        
        st.session_state.recommended_tags = []
        st.session_state.selected_tags = []

    else:
        st.error(f"저장 실패 ({response.status_code})")
        st.write(response.text)


st.divider()


# AI 취향 분석 버튼
if st.button("📊 취향 분석"):
    if not username.strip():
        st.warning("닉네임을 입력해주세요.")
        st.stop()

    with st.spinner("AI가 취향을 분석하는 중입니다..."):
        response = requests.get(
            f"{API_URL}/analyze",
            params={"username": username}
        )

        result = response.json()

    if "message" in result:
            st.warning(result["message"])
    else:
            st.subheader("📊 분석 결과")
            st.write(result["analysis"])


# AI 음악 추천 버튼
if st.button("🎵 음악 추천"):
    if not username.strip():
        st.warning("닉네임을 입력해주세요.")
        st.stop()

    with st.spinner("AI가 음악을 추천하는 중입니다..."):
        response = requests.get(f"{API_URL}/recommend", params={"username": username})

        result = response.json()

    if "message" in result:
        st.warning(result["message"])
    else:
        st.subheader("🎧 AI 추천 음악")
        st.write(result["recommend_music"])