
# ImageFilter for using filter() function
from PIL import Image, ImageFilter

# Opening the image
# (R prefixed to string in order to deal with '\' in paths)
image = Image.open(r"\CodeTest\opencvtetst\chicky_512.png").convert('L')

# Cropping the image 
# smol_image = image.crop((0, 0, 150, 150))

# Blurring image by sending the ImageFilter.
# GaussianBlur predefined kernel argument
# image = image.filter(ImageFilter.GaussianBlur)
image = image

# Pasting the blurred image on the original image
# image.paste(blurred_image, (0,0))

# Displaying the image
image.show()
