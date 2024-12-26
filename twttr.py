def main():
    text_in = input("Input: ")
    text_out = shorten(text_in)
    print(f"Output: {text_out}")


def shorten(word):
    text_out = ""
    for i in range(len(word)):
        if word[i] not in ["a","e","i","o","u", "A","E","I","O","U"]:
            text_out = text_out + word[i]
    return text_out


if __name__ == "__main__":
    main()
