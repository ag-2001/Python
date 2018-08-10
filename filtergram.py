import filters

def main():
    filename = input("Enter an image file to edit: ")
    im = filters.load_img(filename)
    filters.save_img(im, "picture.jpg")
    filters.show_img(im)
    pic = filters.obamicon(im)
    filters.show_img(pic)
main()
