# FastAPI 서버 실행

from fastapi import FastAPI
from pydantic import BaseModel

from .data_loader import load_music_data
from .analysis import analyze_music_data
from .llm import (recommend_tags, generate_music_analysis, recommend_music)

app = FastAPI()


class MusicRequest(BaseModel):
    title: str
    artist: str
    memo: str = ""


@app.get("/")
def root():
    return {"message": "Music Knowledge Base API"}

# 음악 데이터 입력 시 태그 추천
@app.post("/recommend-tags")
def recommend(request: MusicRequest):
    tags = recommend_tags(
        request.title,
        request.artist,
        request.memo
    )

    return {
        "tags": tags
        }

# 사용자 음악 분석
@app.get("/analyze")
def analyze():
    df = load_music_data()
    stats = analyze_music_data(df)
    result = generate_music_analysis(stats)
    return {"analysis": result}

# 사용자 음악 추천
@app.get("/recommend")
def recommend():
    df = load_music_data()
    stats = analyze_music_data(df)
    recommended_music = recommend_music(stats)
    return {"recommended_music": recommended_music}