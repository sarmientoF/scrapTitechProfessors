import json

listOfFiles = ["json/list_chem25494.json", 
"json/list_eps25359.json",  
"json/list_mech26180_2.json",
"json/list_sc_26181.json",  
"json/list-ee26238.json",   
"json/list_ict26182_2.json",
"json/list-iee26523-2.json",
"json/list-mat26105.json",  
"json/list_cap_26183.json", 
"json/list_is25357_2.json", 
"json/list-cs26592.json",   
"json/list-ai26593.json",   
"json/list_bio26393.json",  
"json/list_arch25660.json", 
"json/list_udbe26288.json", 
"json/list_cv26184.json",   
"json/list-gedes26106.json",
"json/list_shs25588_2.json",
"json/list-isc26164.json",  
"json/list-tim26166.json",  
"json/list-ene26107.json",  
"json/list-esd26550.json",  
"json/list_hcsbe_26394.json",
"json/list_ne26139.json"]

def LoadJsons():
  for file in listOfFiles:
    loadFile(file)

def loadFile(file):
  with open(file, 'r') as json_file:
    data = json.load(json_file)
  return data

if __name__ == "__main__":
    data = loadFile(listOfFiles[0])
    
    for key in data["data"]:
      print(key)
