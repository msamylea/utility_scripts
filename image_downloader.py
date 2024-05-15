from simple_image_download import Downloader 
import simple_image_download as simp

# Creating a response object
response = simp.Downloader

## Keyword
keyword = "street+fashion"

# Downloading images
try:
    response().download(keyword, 80)
    print("Images downloaded successfully.")
except Exception as e:
    print("An error occurred:", e)