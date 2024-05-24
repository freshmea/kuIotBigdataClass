import urllib.request

url = "https://avatars.githubusercontent.com/u/78285681?v=4"

print("Start Download")
frame, header = urllib.request.urlretrieve(url, "78285681?v=4")


print("End Download")