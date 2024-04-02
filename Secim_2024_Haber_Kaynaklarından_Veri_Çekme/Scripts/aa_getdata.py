import requests
import json
import time


def fetch_and_store_data():
    # Verileri al
    response = requests.get("https://secim.aa.com.tr/data/result-short.json",verify=False)
    election_data = response.json()
   
    with open("./Data/ANADOLUAJANSI/AA_Secim_2024_Data.json","w",encoding='utf-8') as file:
            json.dump(election_data,file,ensure_ascii=False)
   
    print("Veriler Kaydedildi.")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
fetch_and_store_data()