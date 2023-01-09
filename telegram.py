from tracemalloc import start
import requests, time


from pyrogram.errors import *
from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery, InlineQueryResultArticle, InputTextMessageContent
from pyrogram.session import Session
import time
from time import gmtime, strftime
from threading import Timer,Thread
import uuid
import subprocess
from subprocess import Popen,PIPE
from gtts import gTTS
import requests
import json
import re, sqlite3
from pyrogram.errors import UserNotParticipant 
from pyrogram.types import Message, ChatPermissions
Filters=filters

app = Client(
    "process",
    api_id =  ,
    api_hash = "Masukin Api Hash Dari Telegram.org",
    bot_token = "Masukin Bot Token Dari Botfather")
phoneAPI = ''
admin_id = []
Session.notice_displayed = True
print("OK")

def callback_data_filter(data):
    return filters.create(
        lambda flt, __, query: flt.data == query.data,
        data=data
    )

from requests import get
@app.on_message(filters.command("start") & filters.private)
async def start_command(client, message):  
#
        start_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '💳 BELI VIP 💳', callback_data = 'homecompra')],
    [InlineKeyboardButton(text = '⚙️ CONTROL PANEL ⚙️', callback_data = 'pannellodiamministrazione')],
    ])
        await app.send_message(chat_id = message.chat.id, text =  f'''Halo, selamat datang di bot Anda''', parse_mode = "html", reply_markup = start_btn)  

@app.on_callback_query(callback_data_filter("home"))
def homesdfas(_, query):
    start_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '💳 VIP 💳', callback_data = 'homecompra')],
    [InlineKeyboardButton(text = '⚙️ CONTROL PANEL ⚙️', callback_data = 'pannellodiamministrazione')],
    ])
    query.message.edit(f'**Halo, selamat datang di bot Anda**', reply_markup = start_btn)

@app.on_callback_query(callback_data_filter("homecompra"))
def homecompra(_, query):
    back_to_start_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '📲 Telegram', callback_data = 'telegramvoip')],
    ])
    query.message.edit(f'🔎 Pilih layanan yang akan Anda gunakan VoIP', reply_markup = back_to_start_btn)

@app.on_callback_query(callback_data_filter("pannellodiamministrazione"))
def pannellodiamministrazione(_, query):
    url = 'https://sms-activate.ru/stubs/handler_api.php'
    balance_param = (('api_key', phoneAPI),
                              ('action', 'getBalance'))
    bilancio = float(str(get(url,
                                params=balance_param).text).split(":")[-1])
    back_to_start_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = f'💳 Saldo {bilancio} RUB', callback_data = 'saldo')],
    [InlineKeyboardButton(text = f'🔝 Website', url = 'https://sms-activate.ru/es/buy')],
    [InlineKeyboardButton(text = f'👮‍♂️ Admin', callback_data = 'admin')],
    [InlineKeyboardButton(text = '🏘 Back To Menu 🏘', callback_data = 'home')],
    ])
    query.message.edit(f'**⚙️ CONTROL PANEL ⚙️**', reply_markup = back_to_start_btn)

@app.on_callback_query(callback_data_filter("admin"))
def admin(_, query):
    query.answer('Proses...')

@app.on_callback_query(callback_data_filter("saldo"))
def saldo(_, query):
    query.answer('Saldo...')

@app.on_callback_query(callback_data_filter("telegramvoip"))
def telegramvoip(_, query):
    back_to_start_btn = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text = '🇮🇩 Indonesia', callback_data = 'indonesia_tg'), InlineKeyboardButton(text = '🇷🇴 Romania', callback_data = 'romania_tg')],
    [InlineKeyboardButton(text = '🇬🇭 Ghana', callback_data = 'ghana_tg'), InlineKeyboardButton(text = '''🇨🇮 Costa D'avorio''', callback_data = 'costa_tg')],
    [InlineKeyboardButton(text = '🇮🇹 Italia', callback_data = 'italia_tg'), InlineKeyboardButton(text = '🇺🇸 USA v', callback_data = 'usav_tg')],
    [InlineKeyboardButton(text = '🇨🇦 Canada', callback_data = 'canada_tg'), InlineKeyboardButton(text = '''🇬🇧 Inghilterra''', callback_data = 'uk_tg')],
    [InlineKeyboardButton(text = '🇷🇺 Russia', callback_data = 'russia_tg'), InlineKeyboardButton(text = '''🇬🇧 Francia''', callback_data = 'francia_tg')],
    [InlineKeyboardButton(text = '💲 Costi 💲', url = 'https://telegra.ph/Costi-per-VoIP-01-16')],
    [InlineKeyboardButton(text = '🏘 Back To Menu 🏘', callback_data = 'home')],
    ])
    query.message.edit(f'🔎 Pilih negara VoIP untuk Telegram', reply_markup = back_to_start_btn)

@app.on_callback_query(callback_data_filter("francia_tg"))
async def francia_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=78').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Nomor: +{number} !''') 
    await coppa(query, message)

@app.on_callback_query(callback_data_filter("russia_tg"))
async def russia_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=0').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Nomor: +{number} !''') 
    await coppa(query, message)

@app.on_callback_query(callback_data_filter("canada_tg"))
async def canada_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=36').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Nomor: +{number} !''') 
    await coppa(query, message)
    
@app.on_callback_query(callback_data_filter("uk_tg"))
async def uk_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=12').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Numero: +{number} !''') 
    await coppa(query, message)

@app.on_callback_query(callback_data_filter("usav_tg"))
async def usav_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=12').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Numero: +{number} !''') 
    await coppa(query, message)

@app.on_callback_query(callback_data_filter("italia_tg"))
async def italia_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=86').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Numero: +{number} !''') 
    await coppa(query, message)


@app.on_callback_query(callback_data_filter("indonesia_tg"))
async def indonesia_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=6').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Numero: +{number} !''') 
    await coppa(query, message)

@app.on_callback_query(callback_data_filter("romania_tg"))
async def romania_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=32').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Numero: +{number} !''') 
    await coppa(query, message)

@app.on_callback_query(callback_data_filter("ghana_tg"))
async def ghana_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=38').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Numero: +{number} !''') 
    await coppa(query, message)

@app.on_callback_query(callback_data_filter("costa_tg"))
async def costa_tg(message, query):
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=27').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {query.from_user.id} | {id} | {number}')
    idutente = f'{query.from_user.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await query.message.edit(text =  f'''**✅ Nomor yang dibeli** | ({id})

☎️ Numero: +{number} !''') 
    await coppa(query, message)

async def coppa(query, message):
        global idnumero
        global idutente
        print('Processo coppa startato')
        requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=setStatus&status=1&id=' + idnumero)
        tries = 0
        while tries < 50:
            time.sleep(3)
            res = await get_code(query, message)
            if res is not False:
                done()
                print(f'doneeee ({idnumero})')
                return res
            tries += 1
        banned()
        query.message.edit(text = f'''**❌ Nessun codice ricevuto** | ({idnumero})

☎️ Numero: {numero}
__ℹ️ Anda telah melampaui batas waktu [150 secondi], il VoIP è stato revocato e il saldo è stato riaggiunto__''') 
        return False 

async def get_code(query, message):
    global idnumero
    global idutente
    print(f'kode yang dibutuhkan oleh {idutente}')
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getStatus&id=' + idnumero).text
    if 'STATUS_OK' not in response:
        print(f'STATUS_OK ({idnumero})')
        return False
    print('getcode')
    print(f'possibile code {response}')
    code = response.split(':')[1]
    await app.send_message(chat_id = idutente, text =  f'''**✅ Codice ricevuto** | ({idnumero}) 
    
☎️ Numero: +{numero} 
🔢 Codice: {code}''')
    return response.split(':')[1]

def done() -> None:
    global idnumero
    requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=setStatus&status=6&id=' + idnumero)
    print(f'ddddone ({idnumero})')

def banned() -> None:
    global idnumero
    requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=setStatus&status=8&id=' + idnumero)
    print(f'banned ({idnumero})')


'''
@app.on_message(filters.command("compra") & filters.private)
async def buynum(client, message): 
    global idnumero
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getNumber&service=tg&ref=1194982&country=6').text
    if ":" not in response:
        Exception(response)
    number = response.split(':')[2]
    id = response.split(':')[1]
    pass
    print(f'Pembelian baru dari {message.chat.id} | {id} | {number}')
    idutente = f'{message.chat.id}'
    idnumero = f'{id}'
    numero = f'{number}'
    await app.send_message(chat_id = message.chat.id, text =  f**✅ Nomor yang dibeli** | ({id}) ☎️ Numero: +{number} !) 


@app.on_message(filters.command("code") & filters.private)
async def bugynum(client, message): 
        global idnumero
        global idutente
        requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=setStatus&status=1&id=' + idnumero)
        tries = 0
        while tries < 50:
            time.sleep(3)
            res = await get_code(client, message)
            if res is not False:
                done()
                print(f'doneeee ({idnumero})')
                return res
            tries += 1
        banned()
        await app.send_message(chat_id = idutente, text = f**❌ Nessun codice ricevuto** | ({idnumero})

☎️ Numero: {numero}
__ℹ️ Anda telah melampaui batas waktu [150 secondi], il VoIP è stato revocato e il saldo è stato riaggiunto__) 
        return False 


async def get_code(client, message):
    global idnumero
    print(f'kode yang dibutuhkan oleh {message.chat.id}')
    global idutente
    global numero
    response = requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=getStatus&id=' + idnumero).text
    if 'STATUS_OK' not in response:
        print(f'STATUS_OK ({idnumero})')
        return False
    print('getcode')
    print(f'possibile code {response}')
    code = response.split(':')[1]
    await app.send_message(chat_id = idutente, text = f'**✅ Codice ricevuto** | ({id}) ☎️ Numero: {numero} 🔢 Codice: {code}')
    return response.split(':')[1]

def done() -> None:
    global idnumero
    requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=setStatus&status=6&id=' + idnumero)
    print(f'ddddone ({idnumero})')

def banned() -> None:
    global idnumero
    requests.get('https://api.sms-activate.org/stubs/handler_api.php?api_key=' + phoneAPI + '&action=setStatus&status=8&id=' + idnumero)
    print(f'banned ({idnumero})')

'''
'''
0	Russia
1	Ukraine
2	Kazakhstan
3	China
4	Philippines
5	Myanmar
6	Indonesia
7	Malaysia
8	Kenya
9	Tanzania
10	Vietnam
11	Kyrgyzstan
12	USA (virtual)
13	Israel
14	HongKong
15	Poland
16	England
18	DCongo
19	Nigeria
20	Macao
21	Egypt
22	India
23	Ireland
24	Cambodia
25	Laos
26	Haiti
27	Ivory
28	Gambia
29	Serbia
30	Yemen
31	Southafrica
32	Romania
33	Colombia
34	Estonia
36	Canada
37	Morocco
38	Ghana
39	Argentina
40	Uzbekistan
41	Cameroon
42	Chad
43	Germany
44	Lithuania
45	Croatia
46	Sweden
47	Iraq
48	Netherlands
49	Latvia
50	Austria
51	Belarus
52	Thailand
53	Saudiarabia
54	Mexico
55	Taiwan
56	Spain
58	Algeria
59	Slovenia
60	Bangladesh
61	Senegal
62	Turkey
63	Czech
64	Srilanka
65	Peru
66	Pakistan
67	Newzealand
68	Guinea
69	Mali
70	Venezuela
71	Ethiopia
72	Mongolia
73	Brazil
74	Afghanistan
75	Uganda
76	Angola
77	Cyprus
78	France
79	Papua
80	Mozambique
81	Nepal
82	Belgium
83	Bulgaria
84	Hungary
85	Moldova
86	Italy
87	Paraguay
88	Honduras
89	Tunisia
90	Nicaragua
91	Timorleste
92	Bolivia
93	Costarica
94	Guatemala
95	Uae
96	Zimbabwe
97	Puertorico
99	Togo
100	Kuwait
101	Salvador
102	Libyan
103	Jamaica
104	Trinidad
105	Ecuador
106	Swaziland
107	Oman
108	Bosnia
109	Dominican
111	Qatar
112	Panama
114	Mauritania
115	Sierraleone
116	Jordan
117	Portugal
118	Barbados
119	Burundi
120	Benin
121	Brunei
122	Bahamas
123	Botswana
124	Belize
125	Caf
126	Dominica
127	Grenada
128	Georgia
129	Greece
130	Guineabissau
131	Guyana
132	Iceland
133	Comoros
134	Saintkitts
135	Liberia
136	Lesotho
137	Malawi
138	Namibia
139	Niger
140	Rwanda
141	Slovakia
142	Suriname
143	Tajikistan
144	Monaco
145	Bahrain
146	Reunion
147	Zambia
148	Armenia
149	Somalia
150	Congo
151	Chile
152	Furkinafaso
153	Lebanon
154	Gabon
155	Albania
156	Uruguay
157	Mauritius
158	Bhutan
159	Maldives
160	Guadeloupe
161	Turkmenistan
162	Frenchguiana
163	Finland
164	Saintlucia
165	Luxembourg
166	Saintvincentgrenadines
167	Equatorialguinea
168	Djibouti
169	Antiguabarbuda
170	Caymanislands
171	Montenegro
172	Denmark
173	Switzerland
174	Norway
175	Australia
176	Eritrea
177	Southsudan
178	Saotomeandprincipe
179	Aruba
180	Montserrat
181	Anguilla
183	Northmacedonia
184	Seychelles
185	Newcaledonia
186	Capeverde
187	USA
'''
app.run()
