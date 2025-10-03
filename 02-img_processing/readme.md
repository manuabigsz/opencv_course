hsl - cylinder model
- HUE
- SATURATION
- LIGHTNESS

blending images is done throught the addWeifhted function that uses both images and combines them.
To blend images we use a simple formula:
new_pixel = alpha * pixel_1 + beta * picel_2 + Y

thresholding is fundamentally a very simples method of segmenting an image into different parts
thresholding will convert an image to consist of only two values, white or black