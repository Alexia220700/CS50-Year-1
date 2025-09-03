# ask for input to check the file
file = input("Input file name: ")
# make it lower and without spaces
file = file.lower().strip()

# check the end of the string and output the type of the file it is
if (file.endswith(".gif")):
    print("image/gif")
elif(file.endswith(".jpg") or file.endswith(".jpeg")):
    print("image/jpeg")
elif(file.endswith(".png")):
    print("image/png")
elif(file.endswith(".pdf")):
    print("application/pdf")
elif(file.endswith(".txt")):
    print("text/plain")
elif(file.endswith(".zip")):
    print("application/zip")
# if the file type doesn't match, show this
else:
    print("application/octet-stream")








