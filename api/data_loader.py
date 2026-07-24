# CSV 읽기 및 전처리

from pathlib import Path
import pandas as pd

# 저장 폴더 설정 및 생성
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)


# CSV 파일에서 음악 데이터 불러오기
def load_music_data(username):
    data_path = DATA_DIR / f"{username}.csv"

    if not data_path.exists():
        df = pd.DataFrame(columns=[
            "Title",
            "Artist",
            "Country",
            "Vocal",
            "Since",
            "Tags",
            "Memo"
        ])

        df.to_csv(data_path, index=False)

    df = pd.read_csv(data_path)

    df["Memo"] = df["Memo"].fillna("")
    df["Tags"] = df["Tags"].apply(lambda x: [tag.strip() for tag in str(x).split(",")] if str(x) != "nan" else [])

    return df


# 음악 데이터를 CSV 파일에 추가 업데이트
def save_music_data(username, new_music):
    data_path = DATA_DIR / f"{username}.csv"

    df = load_music_data(username)
    new_df = pd.DataFrame([new_music])
    df = pd.concat([df, new_df], ignore_index=True)
    df.to_csv(data_path, index=False)