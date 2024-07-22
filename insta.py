import  instaloader 
insta=instaloader,instaloader()
username=input("Can yopu please put your username:")

profile = instaloader.Profile.from_username(insta.context, username)
print("Username", profile.username)
print("Number of posts", profile.mediacount)
print("Number of followers", profile.followers)