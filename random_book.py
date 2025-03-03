import requests
from bs4 import BeautifulSoup
import random
import re

def get_random_jpeg(url):
    # Send HTTP GET request to the website
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all image tags on the page
    image_tags = soup.find_all('img')

    jpeg_images = []

    # Filter the image tags to include only JPEG images
    for img in image_tags:
        src = img.get('src')
        if src and re.match(r'.*\.jpe?g$', src, re.I):
            jpeg_images.append(img)

    if len(jpeg_images) > 0:
        # Choose a random JPEG image from the list
        random_jpeg = random.choice(jpeg_images)

        # Extract the source URL of the image
        image_url = random_jpeg['src']

        # Download the image
        response = requests.get(image_url)

        # Save the image to a file
        with open('random_image.jpg', 'wb') as f:
            f.write(response.content)

        print("Random JPEG image downloaded successfully.")
        print(jpeg_images)
    else:
        print("No JPEG images found on the page.")
        
        
        
        
get_random_jpeg("https://www.amazon.com/hz/wishlist/ls/18P8SVU63ZRWI?ref_=list_d_wl_lfu_nav_4")
