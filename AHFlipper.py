import requests
a = 1
Items = []
URL = "https://api.hypixel.net/skyblock/auctions?page="+str(a)
response = requests.get(URL).json()
Budget = int(input("What is your budget? "))
Price = Budget
itemList = []
AH = response["auctions"]
totalAuctions = int(response["totalPages"])
def AHSEARCH(AH):
    for i in range(len(AH)):
        try:
            if AH[i]["bin"]:
                if que2.lower() == AH[i]["item_name"].lower():
                    Items.append([AH[i]["item_name"],AH[i]["starting_bid"]])
                else:
                    pass
            else:
                pass
        except KeyError:
            pass
def getAH(AH):
    for i in range(len(AH)):
        try:
            if AH[i]["bin"]:
                if AH[i]["item_name"] != "Enchanted Book":
                    Items.append([AH[i]["item_name"],AH[i]["starting_bid"]])
                else:
                    pass
        except KeyError:
            pass
que1 = input("Would you like to search for a specific item or look for flips? Type 1 for the item and 2 for the flips and 3 for all items! ")
if que1 == "1":
    que2 = input("What item are you looking for? ")
    for i in range(totalAuctions):
        AHSEARCH(AH)
        a += 1
        URL = "https://api.hypixel.net/skyblock/auctions?page="+str(a)
        response = requests.get(URL).json()
        try:
            AH = response["auctions"]
        except KeyError:
            pass
    Items.sort()
    for i in range(len(Items)):
        print(Items[i])
elif que1 == "2":
    for i in range(totalAuctions):
        getAH(AH)
        a += 1
        URL = "https://api.hypixel.net/skyblock/auctions?page="+str(a)
        response = requests.get(URL).json()
        try:
            AH = response["auctions"]
        except KeyError:
            pass
    Items.sort()
    for i in range(len(Items)):
        try:
            if Items[i][0] == Items[i+1][0]:
                if (Items[i][1]) < Items[i+1][1]:
                    print(Items[i])
                    if (Items[i][1] < Price) and (Items[i][1] != Items[i+1][1]):
                        Price = Items[i][1]
                        itemList.append(Items[i])
                    else:
                        pass
                else:
                    pass
            else:
                Price = Budget
        except IndexError:
            pass
    for i in itemList:
        print(i)
elif que1 == "3":
    for i in range(totalAuctions):
        getAH(AH)
        a += 1
        URL = "https://api.hypixel.net/skyblock/auctions?page="+str(a)
        response = requests.get(URL).json()
        try:
            AH = response["auctions"]
        except KeyError:
            pass
    Items.sort()
    for i in range(len(Items)):
       print(Items[i])
