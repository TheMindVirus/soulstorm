import x2obj, os

print("[INFO]: Decoding X-Files...")
try:
    os.mkdir("./input/")
except:
    pass
try:
    os.mkdir("./output/")
except:
    pass
files = []
for file in os.listdir("./input/"):
    if file.endswith(".x"):
        files.append("./input/" + file)
for filename in files:
    file = open(filename, "r")
    data = file.read()
    file.close()
    x2obj.decode(data)
print("[INFO]: Master Rahool's Work is Done.")
