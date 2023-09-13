import lib


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

print(templates[template].url)

driver = lib.loadDriver({"browser": "Firefox"})
lib.createMeme(driver, text, templates[template].url)