from datetime import datetime
import os

def assess_mood():
    mood_list = [
        ("happy", 2), 
        ("relaxed", 1), 
        ("apathetic", 0), 
        ("sad", -1), 
        ("angry", -2)
    ]
    
    today = datetime.today().strftime('%Y-%m-%d')
    
    data_dir = 'data'
    mood_file = f'{data_dir}/mood_diary.txt'
    
    try:
        with open(mood_file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if today in line:
                    print("Sorry, you have already entered your mood today.")
                    return
    except FileNotFoundError:
        os.makedirs(data_dir, exist_ok=True)
        open(mood_file, 'w').close()
    
    while True:
        mood_today = input("Enter your mood today: ")
        for mood, number in mood_list:
            if mood_today == mood:
                with open(mood_file, 'a') as file:
                    file.write(f"{today}: {number}\n")
                analyze_moods()
                return

def check_file():
    data_dir = 'data'
    mood_file = f'{data_dir}/mood_diary.txt'
    try:
        with open(mood_file, 'r') as file:
            lines = file.readlines()
            if len(lines) >= 7:
                return lines[-7:]
            else:
                return []
    except FileNotFoundError:
        return []

def analyze_moods():
    last_lines = check_file()
    if not last_lines:
        return

    mood_scores = []
    for line in last_lines:
        if line.strip():
            parts = line.strip().split(': ')
            if len(parts) == 2:
                number_part = parts[1]
                mood_scores.append(int(number_part))

    if len(mood_scores) == 0:
        return

    mood_count = {
        "happy": 0,
        "sad": 0,
        "apathetic": 0,
        "relaxed": 0,
        "angry": 0
    }

    for score in mood_scores:
        for mood, value in [("happy", 2), ("relaxed", 1), ("apathetic", 0), ("sad", -1), ("angry", -2)]:
            if score == value:
                mood_count[mood] += 1

    if mood_count["happy"] >= 5:
        print("Your diagnosis: manic!")
    elif mood_count["sad"] >= 4:
        print("Your diagnosis: depressive!")
    elif mood_count["apathetic"] >= 6:
        print("Your diagnosis: schizoid!")
    else:
        average_score = round(sum(mood_scores) / len(mood_scores))
        for mood, value in [("happy", 2), ("relaxed", 1), ("apathetic", 0), ("sad", -1), ("angry", -2)]:
            if average_score == value:
                print(f"Your diagnosis: {mood}!")