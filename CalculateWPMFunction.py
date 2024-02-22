def calculate_wpm(words_typed, time_taken):
    wpm = (words_typed / 5) / (time_taken / 60)  # Assuming 5 words per sentence
    return wpm