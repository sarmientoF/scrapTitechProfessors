import pandas
import json
import os

engHeaders ="index	siteName	code	job	jobCode	lastName	firstName	category	lastNameHiragana	firstNameHiragana	categoryNumber	firstNameEnglish	lastNameEnglish	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	selection	selectionCode	url	url	id		lastNameKatakana	firstNameKatakana				\n"

listOfUrls = ["/graduate_school/faculty/faculty_list/list_phys26382.txt", 
"/graduate_school/faculty/faculty_list/list_chem25494.txt", 
"/graduate_school/faculty/faculty_list/list_eps25359.txt",  
"/graduate_school/faculty/faculty_list/list_mech26180_2.txt",
"/graduate_school/faculty/faculty_list/list_sc_26181.txt",  
"/graduate_school/faculty/faculty_list/list-ee26238.txt",   
"/graduate_school/faculty/faculty_list/list_ict26182_2.txt",
"/graduate_school/faculty/faculty_list/list-iee26523-2.txt",
"/graduate_school/faculty/faculty_list/list-mat26105.txt",  
"/graduate_school/faculty/faculty_list/list_cap_26183.txt", 
"/graduate_school/faculty/faculty_list/list_is25357_2.txt", 
"/graduate_school/faculty/faculty_list/list-cs26592.txt",   
"/graduate_school/faculty/faculty_list/list-ai26593.txt",   
"/graduate_school/faculty/faculty_list/list_bio26393.txt",  
"/graduate_school/faculty/faculty_list/list_arch25660.txt", 
"/graduate_school/faculty/faculty_list/list_udbe26288.txt", 
"/graduate_school/faculty/faculty_list/list_cv26184.txt",   
"/graduate_school/faculty/faculty_list/list-gedes26106.txt",
"/graduate_school/faculty/faculty_list/list_shs25588_2.txt",
"/graduate_school/faculty/faculty_list/list-isc26164.txt",  
"/graduate_school/faculty/faculty_list/list-tim26166.txt",  
"/graduate_school/faculty/faculty_list/list-ene26107.txt",  
"/graduate_school/faculty/faculty_list/list-esd26550.txt",  
"/graduate_school/faculty/faculty_list/list_hcsbe_26394.txt",
"/graduate_school/faculty/faculty_list/list_ne26139.txt"]

def fetchAll():
  for url in listOfUrls:
    name = url[38:-3] + "csv"
    link = f"https://www.titech.ac.jp{url}"
    fetchFile(link, name)
    

def fetchFile(url, name):
  path = f"csv/{name}"
  os.system(f"""curl {url} -o {path}""")
  editHeader(name, path)

def editHeader(name, path):
  with open(path, 'r') as fin:
    data = fin.read().splitlines(True)
  with open(path, 'w') as fout:
      fout.writelines(engHeaders)
      fout.writelines(data[5:])

  csv2json(name, path)

def csv2json(name, path):
  csv_file = pandas.read_csv(path, delimiter="\t", dtype=str)

  result = csv_file.to_json(orient = "table")

  parsed = json.loads(result)

  result_string = json.dumps(parsed, indent=4) 

  json_name = name[:-3] + "json"
  f = open(f"json/{json_name}", "w+")
  f.write(result_string)


if __name__ == "__main__":
  fetchAll()
    # editHeader("arch.csv", "csv/list_bio26393.csv")