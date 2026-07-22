# OpenAI 호출

import os
from getpass import getpass
from dotenv import load_dotenv
from openai import OpenAI

# .env 읽기
load_dotenv()

base_url   = os.getenv("MLAPI_BASE_URL", "https://mlapi.run/40cc17ae-a89b-4f12-a7d6-13293180fc87/v1")
api_key    = os.getenv("MLAPI_API_KEY")
model_name = os.getenv("MLAPI_MODEL", "openai/gpt-4o-mini")

if not api_key or api_key.startswith("여기에"):
    api_key = getpass("MLAPI API Key를 입력하세요: ")

client = OpenAI(base_url=base_url, api_key=api_key)


def recommend_tags(title, artist, memo=""):                             # 음악 정보를 받아 태그 추천

    prompt = f"""
다음 음악 정보를 보고
어울리는 태그를 최대 5개 추천해 주세요.

제목: {title}
아티스트: {artist}
메모: {memo}

조건
- 태그만 출력
- 쉼표(,)로 구분
- 최대 5개
"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "당신은 음악 태그 추천 전문가입니다."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

def generate_music_analysis(stats):
    
    prompt = f"""
다음 음악 통계 데이터를 보고

1. 선호 국가

2. 선호 보컬

3. 가장 많이 들은 태그

4. 가장 많이 들은 아티스트

5. 가장 많이 들은 음악 장르

6. 선호 발매년도

를 자연스럽게 6문장 이내로 설명하세요.

나도 몰랐던 내 취향을 깨달을 수 있는

한 줄 설명을 덧붙여 주세요.

"""
    
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "당신은 음악 데이터 분석 전문가입니다."
            },
            {
                "role": "user",
                "content": prompt + str(stats)
            }
        ]
    )
    return response.choices[0].message.content

def recommend_music(stats):
    prompt = f"""
다음 통계를 보고

사용자의 취향에 맞는

실존하는 음악만을

3~5곡을 추천하세요.

없는 곡은 만들지 마세요.

상위 목록의 아티스트를

추천해도 상관 없습니다.

어떤 아티스트를 추천해도 괜찮지만

이미 사용자의 데이터에 있는 음악은

제외하고 추천하세요.

추천 이유도 한 줄씩 적으세요.

{str(stats)}
"""
    
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "system",
                "content": "당신은 음악 추천 전문가입니다."
            },
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return response.choices[0].message.content  