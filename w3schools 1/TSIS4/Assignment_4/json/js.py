import json 
import os 

json_file = os.path.join(os.getcwd(), "sample.json")

with open(r"C:\Users\Lenovo\pp2\w3schools 1\TSIS4\Assignment_4\json\sample.json") as file:
    data=json.load(file)

print("""Interface Status
================================================================================
DN                                                 Description           Speed    MTU  
-------------------------------------------------- --------------------  ------  ------""")

for i in data['imdata']:
    print("{DN:50}{Speed:>30}{MTU:>6}".format(DN = i['l1PhysIf']['attributes']['dn'], Speed=i['l1PhysIf']['attributes']['speed'], MTU=i['l1PhysIf']['attributes']['mtu']))