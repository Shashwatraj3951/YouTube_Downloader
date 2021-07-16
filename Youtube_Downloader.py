import time
import pytube
import pyfiglet
from pytube import YouTube
from tqdm import tqdm

text = pyfiglet.figlet_format("       YouTube Video")
text1 = pyfiglet.figlet_format("        Downloader")    
text2 = pyfiglet.figlet_format("        & Convertor")

print (" ")
print (text)
print (text1)
print (text2)
print ("                          By Shashwat__Raj")
print (" ")

link = input ("Enter url of YouTube Video :- ")
path = input ("Select path for storing video :- ")

yt = YouTube(link)

print ("  ")
print ("Title :- ", yt.title)
print ("Views :- ", yt.views)

sec = yt.length
ty_res = time.gmtime(sec)
res = time.strftime("%H:%M:%S",ty_res)

print ("Duration :- ", res)
print("Rate :- ", yt.rating)
print("Published on :- ", yt.publish_date)
print("Age Restriction :- ", yt.age_restricted)
print ("  ")

print (yt.title, "is downloading.....")

for i in tqdm (range(100)):
  ys = yt.streams.get_highest_resolution()

ys.download(path)

print ("  ")
print (yt.title," is completly downloaded in folder ",path)

input ()
