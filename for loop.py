blog_posts = ["","This some cool shit, look at it", "That time I banged myself", "I think something is wrong with my mental"]

for post in blog_posts:
    if post == "":
        continue
    print(post)

print("-------------------------------------------")
myString = "this is a string"

for char in myString:
    print(char)
print("-------------------------------------------")
for x in range(0,10):
    print(x)
print("-------------------------------------------")

person = {"Name": 'Karen Smith', "Age": 25, "Gender": "Female"}

for key in person:
    print(key, ":", person[key])

print("-------------------------------------------")
blog_posts = {"About Me": ["This some cool shit, look at it", "That time I banged myself", "I think something is wrong with my mental"], 
              "javascript": ["Javascript is cool", "Reacting to React", "I killed my browser with JavaScript"]}

for category in blog_posts:
    print("Posts about ", category)
    for posts in blog_posts[category]:
        print(posts)