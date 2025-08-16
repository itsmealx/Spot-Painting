import colorgram


def get_colors():
    #extracting color from the image using colorgram package
    colors = colorgram.extract("image.jpg", 50)
    rgb_colors = []

    #get 'rgb' separately and assigning to tuple
    for color in colors[6:]: #slicing as indexes 0-5 contains white color
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b

        rgb = (r,g,b)
        rgb_colors.append(rgb) #appending to create a list of tuples

    return rgb_colors

#used for indexing only
# for index, value in enumerate(rgb_colors):
#     print(f"Index {index}: {value}")