import requests
import io
import re

from TikTokAPI import TikTokAPI


# from logger import logger
def tiktok_downloader(url:str):
    # try:
    #     response = requests.get(url, allow_redirects=False)
    #     redirect_url = response.headers['Location']
    #     print(redirect_url)
    #     response = requests.get(redirect_url)
    #     print(response)
    #     video_url = re.search(r'vid: "([^"]+)"', response.text).group(1)
    #     print(video_url)
    #     response = requests.get(video_url)
    #     print(response)
    # except Exception as er:
    #     print(er)


# Создаем экземпляр API TikTok
    api = TikTokAPI()

    # URL-адрес видео TikTok
    url = "https://www.tiktok.com/@username/video/1234567890123456789"

    # Извлекаем идентификатор видео из URL-адреса
    video_id = api.getVideoById(7207419660784946438)

    # Получаем информацию о видео
    # video_info = api.getTikTokById(video_id, language='en-US')

    # Получаем URL-адрес видео
    video_url = video_id['itemInfo']['itemStruct']['video']['downloadAddr']

    # Скачиваем видео
    response = requests.get(video_url)

    # Сохраняем видео в файл
    with open("video.mp4", "wb") as f:
        f.write(response.content)
    # try:
    #     response = requests.get(url, allow_redirects=False)
    #     redirect_url = response.headers['Location']
    #     print(redirect_url)
    # except Exception as ex:
    #     raise ex
    # with TikTokApi() as api:
    #     video = api.video(id="7207419660784946438")

    # # Bytes of the TikTok video
    #     video_data = video.bytes()

    #     with open("out.mp4", "wb") as out_file:
    #         out_file.write(video_data)
    # api = TikTokApi()
    # video_data = api.get_video_by_url(url)
    # video_url = api.get_video_no_watermark(video_data['itemInfo']['itemStruct']['id'])

    # response = requests.get(video_url)
    # if response.ok:
    #     print("ok")
    # else:
    #     print("Not ok")




    
print(tiktok_downloader("https://vm.tiktok.com/ZMYP5XUDd/"))