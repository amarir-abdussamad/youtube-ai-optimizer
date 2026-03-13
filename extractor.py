import yt_dlp

def get_youtube_metadata(url):
    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'dump_single_json': True,
    }

    

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # extarct_info returns a dictionary
            info = ydl.extract_info(url, download=False)
            raw_date = info.get('upload_date')
            metadata = {
                "Title": info.get('title'),
                "views": info.get('view_count'),
                "Description": (info.get('description') or "No description")[:200] + "...",
                "Author": info.get('uploader'),
                "Duration (Seconds)": info.get('duration'),
                
                "Upload Date": f"{raw_date[6:8]}/{raw_date[4:6]}/{raw_date[:4]}" if raw_date else "Unknown"
            }
            return metadata
    except Exception as e:
        print(f"Error fetching metadata: {e}")
        return None

if __name__ == "__main__":
    video_url = input("Enter the URL: ")
    data = get_youtube_metadata(video_url)

    if data:
        for key, value in data.items():
            print(f"**{key}**: {value}")