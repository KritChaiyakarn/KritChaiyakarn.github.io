import diffusers
from PIL import Image, ImageDraw, ImageFont

def text_to_image(text, diffusers_model):
    diffusers = diffusers.load_diffusers(diffusers_model)
    image_data = diffusers.generate(text)
    image = Image.fromarray(image_data)
    image.show()

if __name__=="__main__":
    input_text = "Hello, World"
    diffusers_model = ".."