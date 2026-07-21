# FastAPI 서버 실행

from data_loader import load_music_data
df = load_music_data()

# 데이터 분석
print("총 음악 수: ", len(df))                              # 총 음악 수
print(df["Country"].value_counts())                         # 국가별 음악 수
print(df["Artist"].value_counts().head())                   # 상위 5개 아티스트별 음악 수
print(df["Vocal"].value_counts())                           # 보컬별 음악 수

from collections import Counter

all_tags = []

for tags in df["Tags"]:
    all_tags.extend(tags)

counter = Counter(all_tags)
print(counter.most_common(10))                              # 상위 10개 태그와 개수

# 통계 출력
print(df.head())
print(df.info())
print(df.isnull().sum())

# LLM 호출
from llm import recommend_tags

result = recommend_tags(
    title="View",
    artist="SHINee",
    memo=""
)

print(result)

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Music Knowledge Base API"}