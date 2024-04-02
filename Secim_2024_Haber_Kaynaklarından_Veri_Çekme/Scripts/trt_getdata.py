import requests
import json
import time

URL=[["TurkiyeGeneli","https://2024secim.trthaber.com/result/AA_YerelSecim2024_TurkiyeGeneli.json"],
     ["IlBelediyeBaskanligi","https://2024secim.trthaber.com/result/AA_YerelSecim2024_IlBelediyeBaskanligi.json"],
     ["IlceBelediyeBaskanligi","https://2024secim.trthaber.com/result/AA_YerelSecim2024_IlceBeldeBelediyeBaskanligi.json"]
     ]

def fetch_and_store_data():
    # Verileri al
    for a,i in URL:
        response = requests.get(str(i))
        election_data = response.json()
    
        with open("./Data/TRT/"+a+".json","w",encoding='utf-8') as file:
            json.dump(election_data,file,ensure_ascii=False)
   
    print("Veriler Kaydedildi")
# Belirli aralıklarla verileri al ve MongoDB'ye aktar
fetch_and_store_data()