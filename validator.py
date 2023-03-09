import re

def validate_url(url: str):
    # Regular expression pattern for matching URLs
    url_regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https:// or ftp:// or ftps://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or IP
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    # Check if the URL matches the pattern
    if not re.match(url_regex, url):
        return False
    else:
        return True

    # # Check if the URL is for Instagram, TikTok, or YouTube
    # if 'instagram.com' in url:
    #     return 'Instagram'
    # elif 'tiktok.com' in url:
    #     return 'TikTok'
    # elif 'youtube.com' in url or 'youtu.be' in url:
    #     return 'YouTube'
    # else:
    #     return False
    #nnckdmkd


# print(validate_url('https://youtu.be/IZGKj1mgNDM'))
