import json

def jsonSaveConfig(object):
    jsonObject = json.dumps(object)
    configName = "savedConfigs/config" + object["configName"] + ".json"
    with open("config.json", "w") as file:
        file.write(jsonObject)
    with open(configName, "a") as savedConfig:
        savedConfig.write(jsonObject)
    return True

def jsonReadConfig():
    with open("config.json", "r") as file:
        jsonObject = json.load(file)
    return jsonObject
