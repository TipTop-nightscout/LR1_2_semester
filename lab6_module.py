import re

def process_text(text):
    print("\nЛР 6")
    text_lower = text.lower()
    words = re.findall(r"[a-zA-Zа-яА-ЯёЁіІїЇєЄ]+", text_lower)

    matching = [w for w in words if len(w) > 1 and w[0] == w[-1]]

    if matching:
        print("Words that begin and end with the same letter:")
        for j in matching:
            print(j)
    else:
        print("These words were not found")