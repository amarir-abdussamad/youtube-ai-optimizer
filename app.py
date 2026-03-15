import streamlit as st
from extractor import get_youtube_metadata
from transcriber import download_audio, transcribe_audio
from analyzer import analyze_video


st.title("YouTube Content Analyzer")

url = st.text_input("Enter your YouTube URL here:")

if st.button("Analyze Video"):
    if url:
        if "youtube.com" not in url and "youtu.be" not in url:
            st.error("Please enter a valid YouTube URL!")
            st.stop()
        with st.spinner("Extracting video metadata..."):
            metadata = get_youtube_metadata(url)
        
        if metadata:
            st.success("Metadata extracted successfully!")
            st.write(metadata)

            with st.spinner("Downloading audio..."):
                audio_path = download_audio(url)
            
            if audio_path:
                st.success("Audio downloaded successfully!")

            with st.spinner("Transcribing audio... (this takes a while)"):
                transcript = transcribe_audio(audio_path)

            if transcript:
                st.success("Transcribe completed!")

                with st.spinner("Analyzing with AI..."):
                    analysis = analyze_video(metadata, transcript) 
                
                if analysis:
                    st.success("Analysis completed!")
                    st.markdown(analysis)