import json
import requests
import time

header = {"Authorization": "TOKEN-KEY"}

response = requests.get("https://api.switch-bot.com/v1.0/devices", headers=header)

if str(response) == '<Response [200]>':
    device_list = json.loads(response.text)

    hub_mini = device_list["body"]["deviceList"][0]
    hub_mini_Id = hub_mini["deviceId"]
    
    air_conditioner = device_list["body"]["infraredRemoteList"][0]
    air_conditioner_id = air_conditioner["deviceId"]
    
    light = device_list["body"]["infraredRemoteList"][1]
    light_id = light["deviceId"]
    
    id_list = [hub_mini_Id, air_conditioner_id, light_id]
else:
    print('It could not work.Please check Authorization or import.')

# ----------Command list-------------

on_command = {
    "command":"turnOn",
    "parameter":"default",
    "commandType":"command"
}
off_command = {
    "command":"turnOff",
    "parameter":"default",
    "commandType":"command"
}
temp_up_command = {
    "command":"setAll",
    "parameter":"default",
    "commandType":"26,5,1,on"
}
light_up_command = {
    "command":"brightnessUp",
    "parameter":"default",
    "commandType":"command"
}
light_down_command = {
    "command":"brightnessDown",
    "parameter":"default",
    "commandType":"command"
}
nightlight_command = {
    "command":"brightnessDown",
    "parameter":"default",
    "commandType":"command"
}

#------------ Change the above command to json.----------

on = json.dumps(on_command)
off = json.dumps(off_command)
light_up = json.dumps(light_up_command)
light_down = json.dumps(light_down_command)

#-------------- Define oparating-----------

def operation(id ,parameter):
    url = 'https://api.switch-bot.com/v1.0/devices/'+ id_list[id] +'/commands'
    post_api = requests.post(url, headers=header, data=parameter)
    print(post_api)

def repetition(id ,parameter, times, sleep):
    for i in range (times):
        url = 'https://api.switch-bot.com/v1.0/devices/'+ id_list[id] +'/commands'
        post_api = requests.post(url, headers=header, data=parameter)
        time.sleep(sleep)
        print(post_api)

def device_off():
    for j in range(len(id_list)):
        url = 'https://api.switch-bot.com/v1.0/devices/'+ id_list[j] +'/commands'
        print(url)
        
        post_api = requests.post(url, headers=header, data=off)
        print(post_api)

def device_on():
    for k in range(len(id_list)):
        url = 'https://api.switch-bot.com/v1.0/devices/'+ id_list[k] +'/commands'
        print(url)
        
        post_api = requests.post(url, headers=header, data=on)
        print(post_api)

# operation(1,off)
# repetition(2,on,3,3)
# device_off()