# CSV 읽기 및 전처리

from pathlib import Path
import pandas as pd
    
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "music_archive.csv"


def load_music_data():

    # CSV 읽기
    df = pd.read_csv(DATA_PATH)
    
    # 전처리
    df["Memo"] = df["Memo"].fillna("")                          # 결측치 처리
    df["Tags"] = df["Tags"].apply(                              # 태그 분리
        lambda x: [tag.strip() for tag in str(x).split(",")]
    )

    return df


def save_music_data(new_music):

    # 새 데이터 추가
    new_df = pd.DataFrame([new_music])

    # 기존 데이터와 병합
    df = pd.concat([load_music_data(), new_df], ignore_index=True)

    # CSV로 저장
    df.to_csv(DATA_PATH, index=False)