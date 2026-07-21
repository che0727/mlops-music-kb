# CSV 읽기 및 전처리

from pathlib import Path
import pandas as pd

def load_music_data():
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    DATA_PATH = BASE_DIR / "data" / "music_archive.csv"

    # CSV 읽기
    df = pd.read_csv(DATA_PATH)
    
    # 전처리
    df["Memo"] = df["Memo"].fillna("")                          # 결측치 처리
    df["Tags"] = df["Tags"].apply(                              # 태그 분리
    lambda x: [tag.strip() for tag in str(x).split(",")]
    )

    return df