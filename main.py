import lib
import json

def main():

    config = None

    try:
        with open("./config.json", "r") as f:
            read = f.read()
            if(read == ""):
                config = json.loads('{"browser": ""}')
            else:
                config = json.loads(read)
    except :
        print("config.json not found. Please create an empty file called config.json")
        return

    if(config["browser"] == ""):
        print("Your browser isnt set. Select a browser: \n0: Firefox\n1: Chrome")
        browser = int(input("> "))

        config["browser"] = ["Firefox", "Chrome", "Safari"][browser]

        with open("config.json", "w") as f:
            f.write(json.dumps(config))


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

    driver = None
    with open("config.json", "r") as f:
        driver = lib.loadDriver(f.read())
        
    lib.createMeme(driver, text, templates[template].url)

if(__name__ == "__main__"):
    main()