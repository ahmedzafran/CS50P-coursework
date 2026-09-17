"""
In a file called extensions.py, implement a program that
prompts the user for the name of a file and then outputs that file’s
 media type if the file’s name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all,
output application/octet-stream instead, which is a common default.
"""

def main():
    file = input("please enter a file name: ")
    sieve(file)

def sieve(x):
    x = x.lower().strip()
    if x.endswith("gif"):
        print("image/gif")
    elif x.endswith("jpg"):
        print("image/jpeg")
    elif x.endswith("jpeg"):
        print("image/jpeg")
    elif x.endswith("png"):
        print("image/png")
    elif x.endswith("pdf"):
        print("application/pdf")
    elif x.endswith("txt"):
        print("text/plain")
    elif x.endswith("zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()
