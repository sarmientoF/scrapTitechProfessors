import csv
import json

csvfile = open('math.csv', 'r')
jsonfile = open('file.json', 'w')

fieldnames = ("管理サイト名",
"コード",
"職種名",
"系サイト職種コード",
"姓",
"名",
"種別",
"姓",
"名0",
"種別",
"名",
"姓",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"選択式",
"コード",
"URL",
"URL",
"ＩＤ",
"姓",
"名")
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')