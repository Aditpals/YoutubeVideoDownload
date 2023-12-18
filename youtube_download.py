from pytube import YouTube

# Replace 'youtube_video_url' with the URL of the video you want to download
video_url = ''

try:
    yt = YouTube(video_url)

    video = yt.streams.get_highest_resolution()

    # Download the video
    print(f'Downloading: {yt.title}...')
    video.download()
    print('Download complete!')

except Exception as e:
    print(f'An error occurred: {str(e)}')
