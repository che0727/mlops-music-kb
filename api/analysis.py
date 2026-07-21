# 음악 데이터 분석

from collections import Counter
from .data_loader import load_music_data

def analyze_music_data(df):

    # 데이터 분석
    print("총 음악 수: ", len(df))                              # 총 음악 수
    print(df["Country"].value_counts())                         # 국가별 음악 수
    print(df["Artist"].value_counts().head())                   # 상위 5개 아티스트별 음악 수
    print(df["Vocal"].value_counts())                           # 보컬별 음악 수

    all_tags = []

    for tags in df["Tags"]:
        all_tags.extend(tags)

    counter = Counter(all_tags)
    print(counter.most_common(10))                              # 상위 10개 태그와 개수

    # 통계 출력
    print(df.head())
    print(df.info())
    print(df.isnull().sum())

    analysis_result = {
        "total_music_count": len(df),
        "country_counts": df["Country"].value_counts().to_dict(),
        "top_artists": df["Artist"].value_counts().head().to_dict(),
        "vocal_counts": df["Vocal"].value_counts().to_dict(),
        "top_tags": counter.most_common(10)
    }

    return analysis_result                                              # 음악 데이터 분석 결과 반환