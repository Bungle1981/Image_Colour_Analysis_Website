#Original attempt at getting the RGB values of the image. Always seemed to find near black versions of colours.
def CreateColourPalette(file):
    img = Image.open(file, "r")
    width, height = img.size
    convert_img = img.convert("RGB")
    all_pixels = []
    for y in range(height):
        for x in range(width):
            rgb_pixel_value = img.getpixel((x, y))
            #hex = rgb_to_hex_conv(rgb_pixel_value)
            #all_pixels.append(rgb_pixel_value)
            pixel = {
                "Pixel Co-Ordinates": f'{x},{y}',
                "RGB_value": img.getpixel((x, y)),
                "Hex_Code_Value": rgb_to_hex_conv(rgb_pixel_value)
            }
            all_pixels.append(pixel)
    image_DataFrame = pandas.DataFrame(all_pixels)
    sorted_DF = image_DataFrame["Hex_Code_Value"].value_counts(ascending=False)[:10]
    colour_palette = {}
    for item in range(0, 10):
        colour_palette[item] = {
            "HexValue": sorted_DF.index[item],
            "Count": sorted_DF[item]
         }
    print (colour_palette)
    return colour_palette