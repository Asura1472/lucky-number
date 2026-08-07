import json
import os
import random
from datetime import datetime, timedelta, timezone

KST = timezone(timedelta(hours=9))

ZODIACS = [
    "쥐", "소", "호랑이", "토끼", "용", "뱀",
    "말", "양", "원숭이", "닭", "개", "돼지"
]

OUTPUT_FILE = "today_zodiac.json"


def get_today_kst():
    return datetime.now(KST).strftime("%Y-%m-%d")


def already_generated_today():
    if not os.path.exists(OUTPUT_FILE):
        return False

    try:
        with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
            existing_data = json.load(f)

        return existing_data.get("date") == get_today_kst()

    except (json.JSONDecodeError, OSError):
        return False


def generate_data():
    now_kst = datetime.now(KST)

    return {
        "date": now_kst.strftime("%Y-%m-%d"),
        "generated_at": now_kst.isoformat(),
        "items": [
            {"zodiac": zodiac, "number": number}
            for zodiac, number in zip(
                ZODIACS,
                random.sample(range(1, 46), 12)
            )
        ]
    }


def main():
    if already_generated_today():
        print("Today's zodiac numbers already generated. Skipping.")
        return

    data = generate_data()

    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Generated zodiac numbers for {data['date']}")


if __name__ == "__main__":
    main()
