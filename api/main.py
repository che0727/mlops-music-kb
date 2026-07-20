from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = BASE_DIR / "data" / "music_archive.csv"

print(DATA_PATH)

df = pd.read_csv(DATA_PATH)

print(df.head())
print(df.info())
print(df.isnull().sum())

df["memo"] = df["memo"].fillna("")
df["tags"] = df["tags"].apply(
    lambda x: [tag.strip() for tag in str(x).split(",")]
)

print("총 음악 수 :", len(df))              # 총 음악 수
print(df["Country"].value_counts())         # 국가별 음악 수
print(df["Artist"].value_counts().head())   # 상위 5개 아티스트별 음악 수

from collections import Counter

all_tags = []

for tags in df["tags"]:
    all_tags.extend(tags)

counter = Counter(all_tags)

print(counter.most_common(10))              # 상위 10개 태그와 개수