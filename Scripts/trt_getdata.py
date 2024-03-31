import requests
from pymongo import MongoClient
import json
import time

URL=[["anlik_veriler-TRT-GENEL","https://2024secim.trthaber.com/result/AA_YerelSecim2024_TurkiyeGeneli.json"],
     ["anlik_veriler-TRT-ilbelediye","https://2024secim.trthaber.com/result/AA_YerelSecim2024_IlBelediyeBaskanligi.json"],
     ["anlik_veriler-TRT-ilcebelediye","https://2024secim.trthaber.com/result/AA_YerelSecim2024_IlceBeldeBelediyeBaskanligi.json"]
     ]


# MongoDB bağlantısı oluştur
client = MongoClient("mongodb://46.101.135.219:27017/")
db = client["secim_verileri"]

def fetch_and_store_data():
    # Verileri al
    for a,i in URL:
        collection = db[a]
        response = requests.get(str(i))
        election_data = response.json()
    
        # Verileri MongoDB'ye aktar
        collection.insert_one(election_data)
   
    print("Veriler MongoDB'ye aktarıldı.")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
while True:
    fetch_and_store_data()
    time.sleep(60)