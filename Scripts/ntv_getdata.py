import requests
from pymongo import MongoClient
import json
import time

# MongoDB bağlantısı oluştur
client = MongoClient("mongodb://46.101.135.219:27017/")
db = client["secim_verileri"]
collection = db["anlik_veriler-NTV"]

def fetch_and_store_data():
    # Verileri al
    for i in range(1,82):
        response = requests.get("https://secim2024-storage.ntv.com.tr/secimsonuc2024/live/parliamentary/"+str(i)+".json")
        election_data = response.json()
    
        # Verileri MongoDB'ye aktar
        collection.insert_one(election_data)
   
    print("Veriler MongoDB'ye aktarıldı.")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
while True:
    fetch_and_store_data()
    time.sleep(60)