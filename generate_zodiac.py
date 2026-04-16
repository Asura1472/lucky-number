import json
import random
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))

ZODIACS = [
    "쥐", "소", "호랑이", "토끼", "용", "뱀",
    "말", "양", "원숭이", "닭", "개", "돼지"
]

def generate_data():
    today_kst = datetime.now(KST).strftime("%Y-%m-%d")

    # 1~45 중 중복 없이 12개
    numbers = random.sample(range(1, 46), 12)

    items = []
    for zodiac, number in zip(ZODIACS, numbers):
        items.append({
            "zodiac": zodiac,
            "number": number
        })

    data = {
        "date": today_kst,
        "items": items
    }

    return data

def main():
    data = generate_data()

    with open("today_zodiac.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
