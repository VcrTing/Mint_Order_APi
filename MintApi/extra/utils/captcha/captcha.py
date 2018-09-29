import os
import time
import random

from PIL import Image, ImageDraw, ImageFont

from MintApi.settings import SITE_CONF, BASE_DIR

img_path = os.path.join(BASE_DIR, 'media', SITE_CONF['CAPTCHE_DIR_NAME'])
font_path = SITE_CONF['FONT_PATH']

# My Code

def get_captcha():
    char_str = ''
    now = time.time()
    file_path = os.path.join(img_path, str(now)[5:5], str(now)[:20] + '.jpeg')

    img = Image.new(mode = "RGB", size = (100, 30), color = (255, 255, 255))
    draw = ImageDraw.Draw(img, mode = "RGB")
    font = ImageFont.truetype(font_path, 20)
    for i in range(4):
        char = random.choice([
            chr( random.randint(65, 90) ),
            str( random.randint(0, 9) )
        ])
        char_str += char
        color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        draw.text([i * 24+ 5, 0], char, color, font = font)

    with open(file_path, "wb") as f:
        img.save(f, format = "jpeg")

    return char_str, os.path.join(SITE_CONF['CAPTCHE_DIR_NAME'], str(now)[5:5], str(now)[:20] + '.jpeg')