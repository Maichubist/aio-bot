import requests
import zipfile
import os
from instaloader import Instaloader, Profile, Post, ConnectionException

L = Instaloader()
# L.login('grigori_downloader', 'Andreipiska22')

def send_profile(user: str):

    try:
        # L.load_session_from_file('maichubist')
        profile = Profile.from_username(L.context, user)
        for post in profile.get_posts():
            L.download_profile(profile)
        
    except ConnectionException as e:
        ...

    if zip_directory(user):
        return True
    return False

def send_photo_inst(url: str):
    pass

def send_video_inst(url: str):
    try:
        post = Post.from_shortcode(L.context, url.split("/")[-2])
        if post.is_video:
            video = requests.get(post.video_url)
            return video.content
        else:
            raise Exception('It is not a video')
    except Exception as er:
        raise er


def zip_directory(profile_name: str):
    with zipfile.ZipFile(f"{profile_name}.zip", 'w', zipfile.ZIP_DEFLATED) as zip_file:
        for root, dirs, files in os.walk(profile_name):
            for file in files:
                if not file.endswith('.xz'):
                    file_path = os.path.join(root, file)
                    zip_file.write(file_path, os.path.relpath(file_path, profile_name))
        return True


# print(send_video_inst('https://www.instagram.com/reel/CntWhFcqQ2k/?igshid=YmMyMTA2M2Y='))
# send_profile('karina_ooww')
