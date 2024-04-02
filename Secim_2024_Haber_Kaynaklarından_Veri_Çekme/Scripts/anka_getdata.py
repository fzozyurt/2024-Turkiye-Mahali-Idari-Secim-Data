import requests
from pymongo import MongoClient
import json
import time
import random

# MongoDB bağlantısı oluştur
client = MongoClient("mongodb://46.101.135.219:27017/")
db = client["secim_verileri"]
collection = db["anlik_veriler-ANKA"]

sehir=["adana",
"adiyaman",
"afyonkarahisar",
"agri",
"amasya",
"ankara",
"antalya",
"artvin",
"aydin",
"balikesir",
"bilecik",
"bingol",
"bitlis",
"bolu",
"burdur",
"bursa",
"canakkale",
"cankiri",
"corum",
"denizli",
"diyarbakir",
"edirne",
"elazig",
"erzincan",
"erzurum",
"eskisehir",
"gaziantep",
"giresun",
"gumushane",
"hakkari",
"hatay",
"isparta",
"mersin",
"istanbul",
"izmir",
"kars",
"kastamonu",
"kayseri",
"kirklareli",
"kirsehir",
"kocaeli",
"konya",
"kutahya",
"malatya",
"manisa",
"kahramanmaras",
"mardin",
"mugla",
"mus",
"nevsehir",
"nigde",
"ordu",
"rize",
"sakarya",
"samsun",
"siirt",
"sinop",
"sivas",
"tekirdag",
"tokat",
"trabzon",
"tunceli",
"sanliurfa",
"usak",
"van",
"yozgat",
"zonguldak",
"aksaray",
"bayburt",
"karaman",
"kirikkale",
"batman",
"sirnak",
"bartin",
"ardahan",
"igdir",
"yalova",
"karabuk",
"kilis",
"osmaniye",
"duzce"
]

user_agent_list = [
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
   "Mozilla/5.0 (iPad; CPU OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/104.0.5112.99 Mobile/15E148 Safari/604.1"
]
reffer_list=[
   'https://secim.ankahaber.net'
]
headers = {
   'Connection': 'keep-alive',
   'Cache-Control': 'max-age=0',
   'Upgrade-Insecure-Requests': '1',
   'User-Agent': random.choice(user_agent_list),
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
   'Accept-Encoding': 'gzip, deflate',
   'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
   'referer': random.choice(reffer_list)
}

def fetch_and_store_data():
    # Verileri al
    for i in range(1,82):

        response = requests.get("https://scdn.ankahaber.net/script/"+str(i)+".json",headers=headers,verify=False)
        response.encoding="utf-8"
        election_data = response.json()         

        with open("./Data/ANKA/"+sehir[i-1]+".json","w",encoding='utf-8') as file:
            json.dump(election_data,file,ensure_ascii=False)
   
    print("Veriler MongoDB'ye aktarıldı.")

fetch_and_store_data()
