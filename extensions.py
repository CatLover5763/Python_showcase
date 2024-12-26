file = input("File name: ").lower()

if file.endswith(".gif") or file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
    category = "image"
elif file.endswith(".txt"):
    category = "text"
else:
    category = "application"
if ".gif" in file:
    file = "gif"
elif ".jpg" in file or ".jpeg" in file:
    file = "jpeg"
elif ".png" in file:
    file = "png"
elif ".pdf" in file:
    file = "pdf"
elif ".zip" in file:
    file = "zip"
elif ".txt" in file:
    file = "plain"
else:
    file = "octet-stream"

print(f"{category}/{file}")
