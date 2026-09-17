from os import path

name = "split.png"
name1 = "j.jpg"

split = path.splitext(name)
print(split[1])

