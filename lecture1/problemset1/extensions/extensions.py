# defining function that return bool true for extensions
def check_gif(n):
    if n.endswith(".gif"):
        return True


def check_jpg(n):
    if n.endswith(".jpg"):
        return True


def check_jpeg(n):
    if n.endswith(".jpeg"):
        return True


def check_png(n):
    if n.endswith(".png"):
        return True


def check_pdf(n):
    if n.endswith(".pdf"):
        return True


def check_txt(n):
    if n.endswith(".txt"):
        return True


def check_zip(n):
    if n.endswith(".zip"):
        return True


# defining a function for main body of program

def main():
    x = input("File Name: ")

    x = x.strip(" ").lower()

# checking for type of extensions using my defined functions
    if check_gif(x) == True:
        print("image/gif")
    elif check_jpg(x) == True:
        print("image/jpeg")
    elif check_jpeg(x) == True:
        print("image/jpeg")
    elif check_png(x) == True:
        print("image/png")
    elif check_pdf(x) == True:
        print("application/pdf")
    elif check_txt(x) == True:
        print("text/plain")
    elif check_zip(x) == True:
        print("application/zip")
    else:
        print("application/octet-stream")


# calling main function
main()
