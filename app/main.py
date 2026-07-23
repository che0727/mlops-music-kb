import streamlit as st
import requests

st.set_page_config(
    page_title="Music Recommendation",
    page_icon="🎵",
    layout="centered"
)

API_URL = "http://127.0.0.1:8000"

st.title("🎵 Music Recommendation System")
st.write("나만의 음악 데이터베이스를 만들고 AI 추천을 받아보세요.")

st.divider()

st.subheader("🎧 음악 정보 입력")

title = st.text_input("제목")
artist = st.text_input("아티스트")

country = st.selectbox(
    "국가",
    ["한국", "미국", "일본", "기타"]
)

vocal = st.selectbox(
    "보컬",
    ["남성", "여성", "혼성", "연주"]
)

since = st.text_input("발매년도")

memo = st.text_area("메모")

tags = st.text_input(
    "태그 (직접 입력 또는 AI 추천)",
    key="tags_input"
)


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
            response = requests.post(
                f"{API_URL}/recommend-tags",
                json=data,
                timeout=30
            )

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

    else:

        st.error(f"추천 실패 ({response.status_code})")
        st.write(response.text)



if st.button("💾 데이터 저장"):

    if not title.strip():
        st.warning("제목을 입력해주세요.")
        st.stop()

    if not artist.strip():
        st.warning("아티스트를 입력해주세요.")
        st.stop()

    data = {
        "title": title,
        "artist": artist,
        "country": country,
        "vocal": vocal,
        "since": since,
        "tags": tags,
        "memo": memo
    }

    try:
        response = requests.post(
            f"{API_URL}/add-music",
            json=data,
            timeout=30
        )

    except requests.exceptions.ConnectionError:
        st.error("FastAPI 서버에 연결할 수 없습니다.")
        st.stop()

    except requests.exceptions.Timeout:
        st.error("응답 시간이 초과되었습니다.")
        st.stop()

    print(response.status_code)
    print(response.text)

    if response.status_code == 200:
        st.success("저장 완료!")
    else:
        st.error(f"저장 실패 ({response.status_code})")
        st.write(response.text)


st.divider()

if st.button("📊 취향 분석"):
    with st.spinner("AI가 취향을 분석하는 중입니다..."):

        response = requests.get(f"{API_URL}/analyze")

    if response.status_code == 200:

        st.subheader("📊 분석 결과")

        st.write(response.json()["analysis"])

    else:

        st.error("분석 실패")


if st.button("🎵 음악 추천"):
    with st.spinner("AI가 음악을 추천하는 중입니다..."):

        response = requests.get(f"{API_URL}/recommend")

    if response.status_code == 200:

        st.subheader("🎧 추천 음악")

        st.write(response.json()["recommended_music"])

    else:

        st.error("추천 실패")
        