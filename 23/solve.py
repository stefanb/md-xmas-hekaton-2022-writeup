#!venv/bin/python3
import requests
from bs4 import BeautifulSoup
from PIL import Image, ImageFilter, ImageOps
from io import BytesIO
import base64
from pytesseract import pytesseract

BaseURL = "https://pisi-bozicku.mojedelo.com/"

prefix="data:image/png;base64,"

page = requests.get(BaseURL)
# print(page)
page.raise_for_status()
soup = BeautifulSoup(page.content, "html.parser")
page.cookies

text_file = open("riddle.html", "w")
n = text_file.write(soup.prettify())
text_file.close()

div = soup.find("div", {"class": "container maze-container"})
# print(div)

images = div.find_all("img")
# print(images)

image1=images[0]
image2=images[1]

im1b64=image1["src"].split(',')[1]
im2b64=image2["src"].split(',')[1]


im1 = Image.open(BytesIO(base64.b64decode(im1b64)))
im2 = Image.open(BytesIO(base64.b64decode(im2b64)))
# im2=im2.filter(ImageFilter.SMOOTH)
# im2 = ImageOps.grayscale(im2)
# im2 = ImageOps.posterize(im2, 1)

im1.save('im1.png')
im2.save('im2.png')

# https://python-bloggers.com/2022/05/extract-text-from-image-using-python/
# https://formulae.brew.sh/formula/tesseract
# brew install tesseract
path_to_tesseract = r'/opt/homebrew/bin/tesseract'
#Define path to image
# path_to_image = 'images/sampletext1-ocr.png'
#Point tessaract_cmd to tessaract.exe
pytesseract.tesseract_cmd = path_to_tesseract
#Open image with PIL
# img = Image.open(path_to_image)
#Extract text from image
# text1 = pytesseract.image_to_string(im1).replace('\n', '').replace(' ', '')
text1 = pytesseract.image_to_string(im1, config="-c tessedit_char_whitelist=01").replace(' ', '')
print(len(text1))
print(text1)
# 10010001100111010111101000101100111001011001000001100011000000100010101010101110001000110010101100001000000001110000011110110010000111100011000011100000001001110000101100000110011111100011101100101100110111011011110111011011100111000010111001011001110100000001010111001000010001000111001100111000110100100111110100010101101110000111101001100111011000011111110000010100001101010010111101101110011011000101011010110001001010111111001011110101111100001001011111011000110000101011101000101100100000101001

print()
# text2 = pytesseract.image_to_string(im2).replace('\n', '').replace(' ', '')
text2 = pytesseract.image_to_string(im2, config="-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ").replace(' ', '')
print(len(text2))
print(text2)

for line in text2.splitlines():
    if len(line)>40:
        print(len(line)-40)
        print(line)
# YYGKOIKNARQRMPZKOGJQSKBUSGUAUUPRNXOVNJDRQEVRTJQMZBZUCBJICQJKCMMNHKAFVZPRIXUTMIKYIAREPLNWLNCCNNHPUAWAJQPSGGNXUZWSFEYNREQHDFWTNTHCGOMLGLNUGIDVVABQJLHZOLESGOEAYCEIXKSTVHMKCDIGFHAYKDSICNRHWBPMPFKPMXPTXHEJAFSKLYUQGMTPMGMRACOBDVNEZQXLDBGCQASFBTNJPHHXJZSXGNAUTRLUCNTTKSVLOBRRJISKWNWVJJHSHRWFUWLZTRUFRFUSFMTPIBSAOBFLXWPVZWZGXBICUELXHBJQEAYMOLPSRKNMBQLTTUANULMUAHMHIYFJILQKACPPTPEVPKYGOMDIBPABVVRLVVLCTEKAXDVSURFTZUQKLGBIXYQKFWFLFQDEPKRREHHFUWSEOTVFJDIPLIOEQIJHHPYOLIMIUQFSWFNENYPUEVAOUFZVZCNIBNTSJPSGINKEJXOYOGS


# binKey

solution=""

for i in range(len(text2)):
    if text1[i % len(text1)]=='1':
        solution = solution + text2[i]
        print(text2[i], end='')

print()
print("solution:")
print(solution)

submit = requests.post("https://pisi-bozicku.mojedelo.com/index.php", cookies= page.cookies, data={"solution": solution})
# print(submit.content)

soup = BeautifulSoup(submit.content, 'html.parser')
print(soup.find("div", {"class": "container alert alert-danger"}))

text_file = open("solution.html", "w")
n = text_file.write(soup.prettify())
text_file.close()
