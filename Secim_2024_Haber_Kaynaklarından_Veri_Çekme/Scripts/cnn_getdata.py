import requests
from pymongo import MongoClient
import json
import time

# MongoDB bağlantısı oluştur
client = MongoClient("mongodb://46.101.135.219:27017/")
db = client["secim_verileri"]
collection = db["anlik_veriler-CNN"]

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
    for i in sehir:
        response = requests.get("https://secim.cnnturk.com/api/mayor/31-mart-2024/city/"+str(i))
        election_data = response.json()
    
        # Verileri MongoDB'ye aktar
        collection.insert_one(election_data)
   
    print("Veriler MongoDB'ye aktarıldı.")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
while True:
    fetch_and_store_data()