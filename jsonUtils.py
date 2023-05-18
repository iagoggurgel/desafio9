import json

def jsonSaveConfig(object):
    jsonObject = json.dumps(object)
    with open("config.json", "w") as file:
        file.write(jsonObject)
    return True

def jsonReadConfig():
    with open("config.json", "r") as file:
        jsonObject = json.load(file)
    return jsonObject
