import requests
from pymongo import MongoClient
import json
import time

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

def fetch_and_store_data():
    # Verileri al
    for i in range(1,82):
        try:
            response = requests.get("https://scdn.ankahaber.net/script/"+str(i)+".json",headers=headers,verify=False)
            response.encoding="utf-8"
            election_data = response.json()
        except:
            response = requests.get("https://scdn.ankahaber.net/script/"+str(i)+".json",headers=headers,verify=False)
            response.encoding="utf-8"
            election_data = response.json()            

        with open("../Data/ANKA/"+sehir[i-1]+".json","w",encoding='utf-8') as file:
            json.dump(election_data,file,ensure_ascii=False)
    
        # Verileri MongoDB'ye aktar
        #collection.insert_one(election_data)
   
    print("Veriler MongoDB'ye aktarıldı.")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
#while True:
fetch_and_store_data()
