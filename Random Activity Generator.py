from random import*

name = input ("what is your name? ")

time = ["10 minutes","20 minutes", "30 minutes", "50m minutes", "1 hour"]
activity = ["play video-games", "go for a Walk", "play football", "listen to music", "watch a movie"]

print("Today" , name , "you will" , choice(activity) , "for" , choice(time))
print( "enjoy" )
