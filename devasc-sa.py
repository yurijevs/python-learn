# Импорт необходимых модулей
import requests
import json
import time

# Используем сохраненный или новый токен?

choice = input("Do you wish to use the hard-coded Webex token? (y/n) ")

if choice == "N" or choice == "n":
    accessToken = input("What is your access token? ")
    accessToken = "Bearer " + accessToken
else:
    accessToken = "Bearer NjNhM2I5NWYtYzc5Mi00MjhkLWEwOWUtNTVkZDg0MWFjOThlYzU3MWEyYzUtZjU1_PE93_d0a60548-d257-4968-b7cc-b4ec8ac374d4"

def WebexMessage(message):
    '''
    Функция отправки сообщений в комнату Webex
    '''
    HTTPHeaders = {
        "Authorization": accessToken,
        "Content-Type": "application/json"
    }
    PostData = {
        "roomId": roomIdToGetMessages,
        "text": message
    }
    r = requests.post("https://webexapis.com/v1/messages", data = json.dumps(PostData), headers = HTTPHeaders)

# Аутентификация на webexapis

r = requests.get("https://webexapis.com/v1/rooms",
                 headers={"Authorization": accessToken}
                 )
if not r.status_code == 200:
    raise Exception("Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))

# Выводим список комнат

print("List of rooms:")
rooms = r.json()["items"]
for room in rooms:
    print("Type: " + room["type"] + ", Name: " + room["title"])

# Спрашиваем пользователя какую комнату будем "мониторить"

while True:
    roomNameToSearch = input("Which room should be monitored for /iss messages? ")
    roomIdToGetMessages = None

    for room in rooms:
        if (room["title"].find(roomNameToSearch) != -1):
            print("Found rooms with the word " + roomNameToSearch)
            print(room["title"])
            roomIdToGetMessages = room["id"]
            roomTitleToGetMessages = room["title"]
            print("Found room : " + roomTitleToGetMessages)
            break
    if (roomIdToGetMessages == None):
        print("Sorry, I didn't find any room with " + roomNameToSearch + " in it.")
        print("Please try again...")
    else:
        break

# Запуск бота и поиск управляющих команд

while True:
    time.sleep(1)
    GetParameters = {
        "roomId": roomIdToGetMessages,
        "max": 1
    }
    r = requests.get("https://webexapis.com/v1/messages",
                     params=GetParameters,
                     headers={"Authorization": accessToken}
                     )
    if not r.status_code == 200:
        raise Exception("Incorrect reply from Webex Teams API. Status code: {}. Text: {}".format(r.status_code, r.text))
    json_data = r.json()
    if len(json_data["items"]) == 0:
        raise Exception("There are no messages in the room.")
    messages = json_data["items"]
    message = messages[0]["text"]
    print("Received message: " + message)

    if message.find("/iss") == 0:
        r_iss = requests.get("http://api.open-notify.org/iss-now.json")
        r_iss_json = r_iss.json()['iss_position']
        coordinate_iss = r_iss_json['latitude'] + ',' + r_iss_json['longitude']
        mapquestkey = "XKBAPlAzcRt8nndHysrB6bGSwY9dxGoA"
        mapquesturl = "https://www.mapquestapi.com/geocoding/v1/reverse"
        headers = {'Content-Type': 'application/json'}
        params = {'location': coordinate_iss, 'key': mapquestkey}
        result = requests.get(mapquesturl, headers=headers, params=params)
        result_json = result.json()['results'][0]['locations'][0]
        print(json.dumps(result_json, indent=4))
        if result_json['adminArea1'] != '':
            WebexMessage("The ISS is moving at close to 28,000 km/h so it's location changes realy fast!")
            responseMessage = '''
            ISS coordinate: {coordinates}
            Country: {country}
            City: {city}
            Street: {street}
            '''.format(coordinates = coordinate_iss, country = result_json['adminArea1'], city = result_json['adminArea5'], street = result_json['street'])
            WebexMessage(responseMessage)
        else:
            responseMessage = "The ISS is moving at close to 28,000 km/h so it's location changes realy fast!"
            WebexMessage(responseMessage)
            responseMessage = '\nISS coorditates: ' + coordinate_iss + '\n' + 'ISS Location: Neutral Earth/Water\n'
            WebexMessage(responseMessage)