import io
import os
import time

from concurrent.futures import ThreadPoolExecutor
import subprocess


import requests
from pytube import YouTube, request
# from pytube import extract, request
from pytube.exceptions import RegexMatchError

from logger.logger import logger
size_threshold = 49_999_999  # 49 MB

def send_video(url: str):
    
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        
        if  stream.filesize > size_threshold:
            logger.info(f'File size is {stream.filesize_mb}, get smaller file')
            stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').first()

        if  stream.filesize > size_threshold:
            logger.error(f'File size is {stream.filesize_mb}| IS A MINIMUM')
            raise Exception('File too large for uploading. Telegram limited us to 50mb')
        
        if not stream:
            logger.error('No video streams found')
            raise Exception("No video streams found")
            
        response = requests.get(stream.url)
        if not response.ok:
            logger.error(f'Got unexpected response | {response.status_code}')
            raise Exception("Failed to download video")
        return io.BytesIO(response.content)
    except RegexMatchError as exx:
        raise exx
    except Exception as ex:
        raise ex
     

def send_audio(url: str):
    try:
        youtube = YouTube(url)

        # Get the audio stream from the video
        audio_stream = youtube.streams.get_audio_only()
        audio_filename = audio_stream.default_filename[:-4]

        if  audio_stream.filesize > size_threshold:
            logger.error(f'File size is {audio_stream.filesize_mb}| IS A MINIMUM')
            raise Exception('File too large for uploading. Telegram limited us to 50mb')
        logger.info(f'File size is {audio_stream.filesize_mb}mb')

        # audio_bytes = io.BytesIO()
        # audio_stream.stream_to_buffer(audio_bytes)
        
        # # Get the bytes of the audio
        # return audio_bytes.getvalue()
        # audio_stream.download

        # Define the download and conversion functions
        def download_audio(audio_stream):
            audio_file = audio_stream.download(output_path="./", filename=audio_filename)
            return audio_file

        def convert_audio(audio_file):
            subprocess.run(['ffmpeg', '-i', audio_file, '-codec:a', 'libmp3lame', '-qscale:a', '2', f'{audio_filename}.mp3'])
            os.remove(audio_file)
            

        # Download and convert the audio file concurrently
        with ThreadPoolExecutor(max_workers=2) as executor:
            download_task = executor.submit(download_audio, audio_stream)
            audio_file = download_task.result()
            convert_task = executor.submit(convert_audio, audio_file)
            convert_task.result()
        return audio_filename
    except Exception as ex:
        raise ex

    



# s = time.perf_counter()
# # # print(send_video('https://youtu.be/IZGKj1mgNDM'))
# send_audio('https://youtu.be/99vdFmw9-Z8')
# elapsed = time.perf_counter() - s
# print(f"executed in {elapsed:0.5f} seconds.")


