from emoji import emojize

user_emoji = input("Input: ")
print(f"Output: {emojize(user_emoji, language='alias')}")
