# 음악 데이터 분석

from collections import Counter

def analyze_music_data(df):

    all_tags = []

    for tags in df["Tags"]:
        all_tags.extend(tags)

    counter = Counter(all_tags)

    analysis_result = {
        "total_music_count": len(df),
        "country_counts": df["Country"].value_counts().to_dict(),
        "top_artists": df["Artist"].value_counts().head().to_dict(),
        "vocal_counts": df["Vocal"].value_counts().to_dict(),
        "since_counts": df["Since"].value_counts().to_dict(),
        "top_tags": counter.most_common(10)
    }

    return analysis_result                                              # 음악 데이터 분석 결과 반환
