import requests
from bs4 import *

animelink = input("Enter Link of your Anime Series : ")  # User Enters URL

start = int(input("Enter Episode Number to start with : "))
end = int(input("Enter Episode Number to end with : "))
print("Generating Links from", start, "to", end )
end=end+1 # Increased by 1 for range function

links = []

animename = animelink.split("/")  # splits link by /
URL_PATTERN = 'https://ww3.gogoanime.io/{}-episode-{}' # General URL pattern for every anime on gogoanime
for episode in range(start,end):
	url = URL_PATTERN.format(animename[4],episode)
	srcCode = requests.get(url).text
	soup = BeautifulSoup(srcCode, 'html.parser')
	link = 'https:'+(soup.find("div", class_="anime_video_body_watch_items").find("iframe").get("src"))
	srcCode = requests.get(link).text
	split = srcCode.split("\n")
	for line in split:
		if("https://vidstreaming.io/goto.php?" in line): # Obtaining link from javascript (probably not the best solution but I couldnt come up with something better than this)
			line = line.replace("                  sources:[{file: '", "")
			line = line.replace("',label: 'HD P','type' : 'mp4'}]", "")
			links.append(line)

f = open("links.txt","w+")

for link in links: # Creating txt file with links
	f.write(link+"\n")

# Note: those are links for mp4 files which you can then download using curl for example