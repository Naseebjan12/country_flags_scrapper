import os
import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

# HTML content (you can also fetch it directly from the URL using requests.get()
with open('flags.html','r') as f:
    html_content = f.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Create a directory to save the images
if not os.path.exists('flags'):
    os.makedirs('flags')

# Find all the flag images and their names
flag_divs = soup.find_all('div', class_='col-md-4')

for div in flag_divs:
    img_tag = div.find('img')
    if img_tag:
        img_url = img_tag['src']
        country_name = div.find('div', style='font-weight:bold; padding-top:10px').text.strip()
        # Download the image
        response = requests.get(f"http://www.worldometers.info{img_url}")
        if response.status_code == 200:
            # Open the image and convert to PNG
            img = Image.open(BytesIO(response.content))
            img_path = os.path.join('flags', f"{country_name}.png")
            img.save(img_path, 'PNG')
            print(f"Saved {country_name}.png")
        else:
            print(f"Failed to download image for {country_name}")