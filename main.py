from rembg import remove
from PIL import Image

input_path = '01.png'
output_path = 'output' + input_path

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
