r = """
v.f30741.ts?start=745730992&end=746126927&type=mpegts&sign=d8c2c2ebcce8a465c8c82fdfffd1bdd4&t=5f28f3d7&us=1640592664578059968
#EXT-X-KEY:METHOD=AES-128,URI="https://ke.qq.com/cgi-bin/qcloud/get_dk?edk=CiCujITT220rnZqKvT3ez0XoieHXE3Q%2FkMPiL9ctB8Dw4RCO08TAChiaoOvUBCokOTMyNDg4YmItOWZjYS00MzFiLWJiYjItNjFmMDhjYjNlYmM3&fileId=5285890804838015784&keySource=VodBuildInKMS&token=dWluPTkzOTE1Nzc2NTt2b2RfdHlwZT0wO2NpZD0xNjc1MjQ5O3Rlcm1faWQ9MTAxNzc1NDc1O3Bsc2tleT0wMDA0MDAwMGM2NzJiMGZlYmE5OWRiM2I1MTVmNjI5NzFiNTI0ZjY0NjM2YTNjYTY2Mjk3YmEyYjVkNmZhNzZiNWU4MjlkNTRkOWU1NTEzZDQzYmI3YTQ4O3Bza2V5PQ%3D%3D",IV=0x00000000000000000000000000000000
#EXTINF:10.000000,
v.f30741.ts?start=746126928&end=746683599&type=mpegts&sign=d8c2c2ebcce8a465c8c82fdfffd1bdd4&t=5f28f3d7&us=1640592664578059968
#EXT-X-KEY:METHOD=AES-128,URI="https://ke.qq.com/cgi-bin/qcloud/get_dk?edk=CiCujITT220rnZqKvT3ez0XoieHXE3Q%2FkMPiL9ctB8Dw4RCO08TAChiaoOvUBCokOTMyNDg4YmItOWZjYS00MzFiLWJiYjItNjFmMDhjYjNlYmM3&fileId=5285890804838015784&keySource=VodBuildInKMS&token=dWluPTkzOTE1Nzc2NTt2b2RfdHlwZT0wO2NpZD0xNjc1MjQ5O3Rlcm1faWQ9MTAxNzc1NDc1O3Bsc2tleT0wMDA0MDAwMGM2NzJiMGZlYmE5OWRiM2I1MTVmNjI5NzFiNTI0ZjY0NjM2YTNjYTY2Mjk3YmEyYjVkNmZhNzZiNWU4MjlkNTRkOWU1NTEzZDQzYmI3YTQ4O3Bza2V5PQ%3D%3D",IV=0x00000000000000000000000000000000
#EXTINF:10.000000,
"""
import re
rule = re.compile('v\.f30741\.ts\?start=[0-9]+&end=[0-9]+&type=mpegts&t=\w+&us=\d+&sign=\w+|'
                  'v\.f30741\.ts\?start=[0-9]+&end=[0-9]+&type=mpegts&sign=\w+&us=\d+&t=\w+|'
                  'v\.f30741\.ts\?start=[0-9]+&end=[0-9]+&type=mpegts&sign=\w+&t=\w+&us=\d+')
print(r)
list_r = re.findall(rule,r)

print(list_r)
