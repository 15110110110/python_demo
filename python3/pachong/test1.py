import requests as re

url = 'https://ugcydzd.qq.com/uwMROfz2r57IIaQXGdGnC2dePkY6TBijNmYhp7I7TbAHYM2s/szg_7894_50001_0b6bh4aaqaaaxeapx3vdsjpvcp6dba7qacca.f622.mp4?sdtfrom=v1105&guid=bb2b32eb7dc6084ab7ff00dbfce9e1cb&vkey=0C14B3C4A8B045EE349102A8A9C753F13AAD79BE8543A0FB32A90DE0A2F9210178797B5EE87F50A5257101D63732B5E3E24C06D55D1AFD045A7F77787D22B5B1F7D2F5EF7144C7E4BC5796458965A2B55392B1D70B2BB819630B126C25E088BBE608F538CABF0453820F7768443E973B2E3004184466B49BF02C282DDBB64429'

data = re.get(url).content

with open('./123.mp4', 'wb') as da_file:
    da_file.write(data)
print('----ok----')