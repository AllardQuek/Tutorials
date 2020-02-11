import requests, json

json_res = requests.get("https://www.threatcrowd.org/searchApi/v2/antivirus/report/", {"antivirus" :"emotet"}).json()
hashes = json_res['hashes']

with open('API_emotet_md5.txt', 'a') as f:
    for h in hashes:
        write_data = f.write(h + '\n')