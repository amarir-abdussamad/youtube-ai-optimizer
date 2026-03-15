import streamlit as st
from extractor import get_youtube_metadata
from transcriber import download_audio, transcribe_audio
from analyzer import analyze_video


st.title("YouTube Content Analyzer")

# Prevent multiple runs when user clicks button multiple times
if "processing" not in st.session_state:
    st.session_state.processing = False

url = st.text_input("Enter your YouTube URL here:")

if st.button("Analyze Video") and not st.session_state.processing:
    st.session_state.processing = True

    if url:
        if "youtube.com" not in url and "youtu.be" not in url:
            st.error("Please enter a valid YouTube URL!")
            st.stop()

        progress = st.progress(0)

        # Step 1: Extract Metadata
        with st.spinner("Extracting video metadata..."):
            metadata = get_youtube_metadata(url)
        progress.progress(25)
        
        if metadata:
            st.success("Metadata extracted successfully!")

            st.subheader("Video Metadata")
            st.write(f"**Title:** {metadata['Title']}")
            st.write(f"**Author:** {metadata['Author']}")
            st.write(f"**Views:** {metadata['views']}")
            st.write(f"**Duration:** {metadata['Duration (Seconds)']} seconds")
            st.write(f"**Upload Date:** {metadata['Upload Date']}")

        else:
            st.error("Failed to extract metadata.")
            st.stop()

        # Step 2: Download Audio

        with st.spinner("Downloading audio..."):
            audio_path = download_audio(url)
        progress.progress(50)

        if audio_path:
            st.success("Audio downloaded successfully!")

        else:
            st.error("Failed to download audio.")
            st.stop()

        # Step 3: Transcribe Audio
        with st.spinner("Transcribing audio... (this takes a while)"):
            transcript = transcribe_audio(audio_path)
        progress.progress(75)

        if transcript:
            st.success("Transcribe completed!")

            with st.expander("Show Transcript"):
                st.write(transcript)
        
        else:
            st.error("Failed to transcribe audio.")
            st.stop()

        # Step 4: AI analysis
        with st.spinner("Analyzing with AI..."):
            analysis = analyze_video(metadata, transcript) 
        progress.progress(100)
                
        if analysis:
            st.success("Analysis completed!")

            st.subheader("AI content suggestions")
            st.markdown(analysis)
    else:
        st.warning("Please enter a YouTube URL.")
    
    st.session_state.processing = False