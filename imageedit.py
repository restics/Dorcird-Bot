from PIL import Image, ImageDraw, ImageFont


"""
Creates a soyjack and chad meme using the given strings,
saves it to a image file
"""


def save_meme(template: Image):
  template.save("copy.png")


def create_meme(soy = "loser", chad = "winner"):
  template = Image.open("chad vs soyjak.png")
  pen = ImageDraw.Draw(template)
  font = ImageFont.truetype("ArialCE.ttf", size=25)
  chad = wrap_text(chad)
  soy = wrap_text(soy)


  for i in range(0, len(chad)):
    pen.text((370,60 + (30 * i)), chad[i], font=font, fill='black')


  for i in range(0, len(soy)):
    pen.text((370,300 + (30 * i)), soy[i], font=font, fill='black')
    

  save_meme(template)




def wrap_text(string):
  string_split = string.split(" ")
  string = [""]
  j = 0
  for i in string_split:
    if (len(string[j]) + len(i) > 36):
      j = j + 1
      string.append("")
    string[j] = string[j] + " " + i
  return string

  
    