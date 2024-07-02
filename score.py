import json

score_file = "high_scores.json"

def save_score(name, score):
    try:
        with open(score_file, "r") as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []

    # Add or update the score for the player
    updated = False
    for entry in scores:
        if entry["name"] == name:
            entry["score"] = max(entry["score"], score)
            updated = True
            break

    if not updated:
        scores.append({"name": name, "score": score})

    scores = sorted(scores, key=lambda x: x["score"], reverse=True)[:10]  # Keep top 10 scores

    with open(score_file, "w") as file:
        json.dump(scores, file)

def get_scores():
    try:
        with open(score_file, "r") as file:
            scores = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        scores = []
    return scores

def get_top_5_scores():
    scores = get_scores()
    return sorted(scores, key=lambda x: x["score"], reverse=True)[:5]
