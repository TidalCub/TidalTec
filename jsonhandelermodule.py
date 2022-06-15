import json

def wholesale(jsonfilter,product):
    f = open('jsonfiles/wholesale.json')
    data = json.load(f)
    result = None
    if product == False:
        for i in range(len(data["catagories"])):
            if data["catagories"][i]["cat"] == jsonfilter:
                result = data["catagories"][i]
    if product == True:
        for i in range(len(data["Products"])):
            if data["Products"][i]["Title"] == jsonfilter:
                result = data["Products"][i]

    return result



data = wholesale("M4 BB Funnel",True)
