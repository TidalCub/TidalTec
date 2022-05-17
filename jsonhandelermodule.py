import json

def wholesale(jsonfilter):
    f = open('jsonfiles/wholesale.json')
    data = json.load(f)
    for i in range(len(data["catagories"])):
        if data["catagories"][i]["cat"] == jsonfilter:
            return data["catagories"][i]
            
    



#wholesale("bbfunnel")