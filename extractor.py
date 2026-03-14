import yt_dlp


def format_date(raw_date):
    if raw_date and len(raw_date) == 8:
        return f"{raw_date[6:8]}/{raw_date[4:6]}/{raw_date[:4]}"
    return "Unknown"

def shorten_text(text, length = 200):
    if not text:
        return "No Description"

    if len(text) <= length:
        return text
    
    return text[:length] + "..."

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
            metadata = {
                "Title": info.get('title'),
                "views": info.get('view_count'),
                "Description": shorten_text(info.get('description')),
                "Author": info.get('uploader'),
                "Duration (Seconds)": info.get('duration'),
                "Upload Date": format_date(info.get('upload_date')),
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