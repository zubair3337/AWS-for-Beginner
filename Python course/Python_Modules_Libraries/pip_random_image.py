import requests

url = "https://picsum.photos/200"  # Random image generator
response = requests.get(url)

if response.status_code == 200:
    with open("random_image.jpg", "wb") as file:
        file.write(response.content)
    print("🖼️ Random image saved as random_image.jpg")
else:
    print("⚠️ Couldn't download the image. Status:", response.status_code)
