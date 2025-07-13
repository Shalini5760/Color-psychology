mood_to_color = {
    "happy": "yellow",
    "sad": "blue",
    "angry": "red",
    "stressed": "blue",
    "relaxed": "green",
    "energetic": "red",
    "confident": "black",
    "caring": "pink",
    "confused":"violet",
    "depressed":"orange"
}

color_to_outfit = {
    "red": "red hoodie or red activewear",
    "blue": "blue jeans or a calming blue shirt",
    "yellow": "yellow sundress or yellow t-shirt",
    "green": "green kurta or a soothing green top",
    "black": "black suit or formal black dress",
    "pink": "pink cardigan or pink top",
    "violet":"violet skirt or violet kurti",
    "orange":"orange gown or orange stain dress"
}

user_mood = input("How are you feeling today? (e.g., happy, sad, energetic): ").strip().lower()

if user_mood in mood_to_color:
    color = mood_to_color[user_mood]
    outfit = color_to_outfit.get(color, "an outfit in your favorite color")
    
    print("\nMood Detected:", user_mood.capitalize())
    print("Recommended Color:", color.capitalize())
    print("Suggested Outfit:", outfit)
else:
    print("Sorry, mood not recognized. Try another mood like happy, sad, stressed, etc.")