from PIL import Image
# Rename this file to be "filters.py"
# Add commands to import modules here.

# Define your load_img() function here.
#       Parameters: The name of the file to be opened (string)
#       Returns: The image object with the opened file.

def load_img(filename):
    image = Image.open(filename)
    return image

# Define your show_img() function here.
#       Parameters: The image object to display.
#       Returns: nothing.
def show_img(picture):
    picture.show()
    #Image.show(picture) DO NOT DO THIS

# Define your save_img() function here.
#       Parameters: The image object to save, the name to save the file as (string)
#       Returns: nothing.
def save_img(filename, name):
    filename.save(name, "jpeg")

# Define your obamicon() function here.
#       Parameters: The image object to apply the filter to.
#       Returns: A New Image object with the filter applied.
def obamicon(image):
    newImage = image
    newImagelist = image.getdata()
    newList = []
    for pixel in newImagelist:
        intensity = pixel[0] + pixel[1] + pixel[2]
        if intensity < 182:
            newList.append((0, 51, 76))
        elif intensity >= 182 and intensity <= 364:
            newList.append((217, 26, 33))
        elif intensity > 364 and intensity <= 546:
            newList.append((112, 50, 158))
        elif intensity > 546:
            newList.append((252, 227, 166))
    newImage.putdata(newList)
    return newImage
