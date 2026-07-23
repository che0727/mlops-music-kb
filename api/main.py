# FastAPI 서버 실행

from fastapi import (FastAPI, HTTPException)
from pydantic import BaseModel

from .data_loader import load_music_data, save_music_data
from .analysis import analyze_music_data
from .llm import (recommend_tags, generate_music_analysis, recommend_music)

app = FastAPI()


class MusicRequest(BaseModel):
    title: str
    artist: str
    memo: str = ""

class SaveMusicRequest(BaseModel):
    username: str
    title: str
    artist: str
    country: str
    vocal: str
    since: str = ""
    tags: str = ""
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
def analyze(username: str):
    try:
        df = load_music_data(username)
        if len(df) < 3:
            return {
                "message": "데이터가 부족합니다. 3곡 이상 입력해주세요."
            }
        
        stats = analyze_music_data(df)
        result = generate_music_analysis(stats)

        return {"analysis": result}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    

# 사용자 음악 추천
@app.get("/recommend")
def recommend_music_api(username: str):
    try:
        df = load_music_data(username)
        if len(df) < 3:
            return {
                "message": "데이터가 부족합니다. 3곡 이상 입력해주세요."
            }
        
        stats = analyze_music_data(df)
        result = recommend_music(stats)

        return {"recommend_music": result}

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
        

# 음악 데이터 저장
@app.post("/add-music")
def add_music(request: SaveMusicRequest):

    new_music = {
        "Title": request.title,
        "Artist": request.artist,
        "Country": request.country,
        "Vocal": request.vocal,
        "Since": request.since,
        "Tags": request.tags,
        "Memo": request.memo
    }
    try:
        save_music_data(
            request.username,
            new_music
        )
        
        df = load_music_data(request.username)

        return {"message": "저장 완료", "count": len(df)}
    
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )