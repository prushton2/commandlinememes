import lib
import json

def main():

    print("Select a browser: \n0: Firefox\n1: Chrome")
    browser = int(input("> "))

    print("Search for a template")
    query = input("> ")

    templates = lib.search(query)

    print("Select a template")
    for j, i in enumerate(templates):
        if(i.name[0:2] != "//"):
            print(f"{j}: {i.name}")

    template = int(input("> "))


    text = []

    print("Enter your captions from top left to bottom right. Double press enter on your last caption")

    ipt = None
    while(ipt != ""):
        ipt = input("> ")
        text.append(ipt)

    text.pop()

    print("Please wait while the meme is generated...")

    # print(templates[template].url)

    driver = lib.loadDriver(browser)

    lib.createMeme(driver, text, templates[template].url)

if(__name__ == "__main__"):
    main()