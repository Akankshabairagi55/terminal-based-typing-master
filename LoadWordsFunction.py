def load_words_from_category(category):
    if category == "animals":
        return ["cat", "dog", "elephant", "lion", "tiger"]
    elif category == "fruits":
        return ["apple", "banana", "orange", "grape", "watermelon"]
    else:
        print("Invalid category. Using default category 'animals'.")
        return ["cat", "dog", "elephant", "lion", "tiger"]