from pytube import YouTube
url = input('enter the video url: ')
destination_folder = input('enter destination directory: ')
youtube_video = YouTube(url)
video_title = youtube_video.title
video_thumnbail =youtube_video.thumbnail_url
# streams
# video_streams = youtube_video.streams.all()
default_stream = youtube_video.streams.first()
# adaptive_stream = youtube_video.streams.filter(adaptive=True).all()
# progressive_stream = youtube_video.streams.filter(progressive=True).all()

def download(stream,destination_folder):
	if destination_folder != '':
		print(f"Downlading {video_title}")
		stream.download(destination_folder)
	else:
		print(f"Downlading {video_title} ")
		stream.download()


download(default_stream,destination_folder)

print(f"Video Title: {video_title}")
print(f"Floder: {destination_folder}")
print(f"Download Video Thumnail at: {video_thumnbail}")





