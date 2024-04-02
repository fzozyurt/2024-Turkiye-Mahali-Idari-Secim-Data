import requests
import json
import time

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
        response = requests.get("https://secim2024-storage.ntv.com.tr/secimsonuc2024/live/parliamentary/"+str(i)+".json",verify=False)
        election_data = response.json()
    
        # Verileri MongoDB'ye aktar
        with open("./Data/NTV/"+sehir[i-1]+".json","w",encoding='utf-8') as file:
            json.dump(election_data,file,ensure_ascii=False)
   
    print("Veriler Kaydedildi")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
fetch_and_store_data()