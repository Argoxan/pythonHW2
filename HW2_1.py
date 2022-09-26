import os

print(os.getcwd())

os.mkdir("NewFolder") #creating a folder

print(os.listdir()) #reading everything inside the folder

os.rmdir("NewFolder") 

print(os.listdir())

os.chdir(r"C:\Users\user\Desktop\Python\Intro") #to change folder