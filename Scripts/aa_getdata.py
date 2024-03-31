import requests
from pymongo import MongoClient
import json
import time

# MongoDB bağlantısı oluştur
client = MongoClient("mongodb://46.101.135.219:27017/")
db = client["secim_verileri"]
collection = db["anlik_veriler"]

def fetch_and_store_data():
    # Verileri al
    response = requests.get("https://secim.aa.com.tr/data/result-short.json")
    election_data = response.json()
   
    # Verileri MongoDB'ye aktar
    collection.insert_one(election_data)
   
    print("Veriler MongoDB'ye aktarıldı.")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
while True:
    fetch_and_store_data()
    time.sleep(60)