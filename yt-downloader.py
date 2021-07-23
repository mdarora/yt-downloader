from pytube import YouTube

url = input("Enter the youtube video's URL : ")

try:
	videos = YouTube(url)

	count = 1;
	print("Loading...")

	for stream in videos.streams:
		print(count,":", stream)
		count+=1

	num = int(input("\nEnter the number of stream you want to download : "));

	print("Downloading...")
	videos.streams[num-1].download("../Downloads")
	print("Download completed.")
except Exception as e:
	print("Something is wrong! Please check your input and try again.")
	print("e")
