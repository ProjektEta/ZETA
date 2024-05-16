import json
import os

def Mod(userid):

    ModData = []

    with open("ModData.json") as fp:
        ModData = json.load(fp)

    ModData.append({"userid": userid})

    with open("ModData.json", "w") as f:
        json.dump(ModData, f, indent=4)

    return

def UnMod(userid):

    ModData = []

    with open("ModData.json") as fp:
        ModData = json.load(fp)

    NewModData = []
    for entry in ModData:
        if entry['userid'] == userid:
            pass
        else:
            NewModData.append(entry)

    with open("ModData.json", "w") as f:
        json.dump(NewModData, f, indent=4)

    return

def isMod(userid):

    ModData = []

    with open("ModData.json") as fp:
        ModData = json.load(fp)

    _IsMod = False

    for entry in ModData:
        if entry['userid'] == userid:
            _IsMod = True

    return _IsMod
