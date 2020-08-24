import requests
import os
import re

# voddrm.token.dWluPTE0NDExNTIxMTk1Njk3OTIyMTt2b2RfdHlwZT0wO2NpZD0xNjc1MjQyO3Rlcm1faWQ9MTAxNzc1NDY4O2V4dD0zZjQxY2IzMjBiZjY0ZGQ1M2RhNzc2MDg3ZDYxYThjNjU5ZDY2ZTVhMDgwZWEzZTIwZTE4ZmNhMWVhNDgyOGIzMWYyZmI0NTYwYjg0NjUyM.m3u8

# https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/21e839925285890804838015784/drm/voddrm.token.dWluPTkzOTE1Nzc2NTt2b2RfdHlwZT0wO2NpZD0xNjc1MjQ5O3Rlcm1faWQ9MTAxNzc1NDc1O3Bsc2tleT0wMDA0MDAwMGM2NzJiMGZlYmE5OWRiM2I1MTVmNjI5NzFiNTI0ZjY0NjM2YTNjYTY2Mjk3YmEyYjVkNmZhNzZiNWU4MjlkNTRkOWU1NTEzZDQzYmI3YTQ4O3Bza2V5PQ==.v.f30741.m3u8?us=5913068789159416434&sign=99bc0e0ef335e79e025062e0365b57ed&exper=0&t=5f28c235
# https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/21e839925285890804838015784/drm/v.f30741.ts?start=580250224&end=581664927&type=mpegts&sign=fb5540cabd41277722f0e34d1fd4e0e9&t=5f28c235&us=5913068789159416434


"""
v.f30741.ts?start=580250224&end=581664927&type=mpegts&sign=fb5540cabd41277722f0e34d1fd4e0e9&t=5f28c235&us=5913068789159416434
#EXT-X-KEY:METHOD=AES-128,URI="https://ke.qq.com/cgi-bin/qcloud/get_dk?edk=CiCujITT220rnZqKvT3ez0XoieHXE3Q%2FkMPiL9ctB8Dw4RCO08TAChiaoOvUBCokOTMyNDg4YmItOWZjYS00MzFiLWJiYjItNjFmMDhjYjNlYmM3&fileId=5285890804838015784&keySource=VodBuildInKMS&token=dWluPTkzOTE1Nzc2NTt2b2RfdHlwZT0wO2NpZD0xNjc1MjQ5O3Rlcm1faWQ9MTAxNzc1NDc1O3Bsc2tleT0wMDA0MDAwMGM2NzJiMGZlYmE5OWRiM2I1MTVmNjI5NzFiNTI0ZjY0NjM2YTNjYTY2Mjk3YmEyYjVkNmZhNzZiNWU4MjlkNTRkOWU1NTEzZDQzYmI3YTQ4O3Bza2V5PQ%3D%3D",IV=0x00000000000000000000000000000000
#EXTINF:10.000000,
"""

url = "https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/21e839925285890804838015784/drm/voddrm.token.dWluPTkzOTE1Nzc2NTt2b2RfdHlwZT0wO2NpZD0xNjc1MjQ5O3Rlcm1faWQ9MTAxNzc1NDc1O3Bsc2tleT0wMDA0MDAwMGM2NzJiMGZlYmE5OWRiM2I1MTVmNjI5NzFiNTI0ZjY0NjM2YTNjYTY2Mjk3YmEyYjVkNmZhNzZiNWU4MjlkNTRkOWU1NTEzZDQzYmI3YTQ4O3Bza2V5PQ==.v.f30741.m3u8?us=5913068789159416434&sign=99bc0e0ef335e79e025062e0365b57ed&exper=0&t=5f28c235"

header = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.87 Safari/537.36",
  "Referer": "https://ke.qq.com/webcourse/index.html",
  "Host": "1258712167.vod2.myqcloud.com"
}

BASE_URL = "https://1258712167.vod2.myqcloud.com/fb8e6c92vodtranscq1258712167/21e839925285890804838015784/drm/"

r = requests.get(url, headers=header).text

rule = re.compile('v\.f30741\.ts\?start=[0-9]+&end=[0-9]+&type=mpegts&t=5f28c235&us=5913068789159416434&sign=fb5540cabd41277722f0e34d1fd4e0e9|v\.f30741\.ts\?start=[0-9]+&end=[0-9]+&type=mpegts&sign=fb5540cabd41277722f0e34d1fd4e0e9&us=5913068789159416434&t=5f28c235')
with open('res.txt','r') as fp:
    end_str = fp.read()


end_str_list = re.findall(rule,end_str)
print(len(end_str_list))
