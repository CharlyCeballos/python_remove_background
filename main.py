from rembg import remove
from PIL import Image

input_path = '02.jpg'
name_file = input_path.split('.')
output_path = 'output' + name_file[0] + '.png'
print(output_path)

input = Image.open(input_path)
output = remove(input)
output.save(output_path)
