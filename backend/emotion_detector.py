
def detect_emotion(text):
    text = text.lower()
    if any(w in text for w in ["happy","great","awesome"]):
        return "Happy"
    elif any(w in text for w in ["sad","cry","bad"]):
        return "Sad"
    elif any(w in text for w in ["angry","hate"]):
        return "Angry"
    return "Neutral"
