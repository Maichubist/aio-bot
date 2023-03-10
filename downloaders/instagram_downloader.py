import requests
from instaloader import Instaloader, Profile, Post
L = Instaloader()
L.login('grigori_downloader', 'Andreipiska22')

def send_profile(u: str):
    
    u = u
    
    try:
        
    
        # L.load_session_from_file('maichubist')
        profile = Profile.from_username(L.context, u)
        for post in profile.get_posts():
            L.download_profile(profile)
        

    except Exception as err:
        print(err)

def send_photo_inst(url: str):
    pass

def send_video_inst(url: str):
    try:
        L = Instaloader()
        post = Post.from_shortcode(L.context, url.split("/")[-2])
        if post.is_video:
            video = requests.get(post.video_url)
            return video.content
        else:
            raise Exception('It is not a video')
    except Exception as er:
        raise er

# print(send_video_inst('https://www.instagram.com/reel/CntWhFcqQ2k/?igshid=YmMyMTA2M2Y='))
# send_profile('viktoriavolyn')