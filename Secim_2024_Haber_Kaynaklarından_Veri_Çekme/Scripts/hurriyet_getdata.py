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
    for i in sehir:
        response = requests.get("https://secim.hurriyet.com.tr/assets/yerel/data/iller/"+str(i)+".json",verify=False)
        election_data = response.json()

        with open("../Data/HURRIYET/"+i+".json","w",encoding='utf-8') as file:
            json.dump(election_data,file,ensure_ascii=False)
    
        # Verileri MongoDB'ye aktar
        #collection.insert_one(election_data)
   
    print("Veriler Kaydedildi")

# Belirli aralıklarla verileri al ve MongoDB'ye aktar
fetch_and_store_data()