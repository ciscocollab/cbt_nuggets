import json

jsonstr = """{"people":[{"id":"1","FirstName":"Benjamin","LastName":"Finkel","Email":"ben.finkel@cbtnuggets.com"},
    {"id":"2","FirstName":"Jane","LastName":"Doe",
    "Email":"jane.doe@cbtnuggets.com"},
    {"id":"3","FirstName":"Pat","LastName":"Smith",
    "Email":"pat.smith@cbtnuggets.com"}]}"""

jsonobj = json.loads(jsonstr)

print(jsonobj['people'][1])

jsonobj = json.load(open('C:\\Users\\pkinane\\Documents\\DevNetAsc_200-901\\my_code\\cbt_nuggets\\cbt_nuggets\\parsing_files\\jsonsample.json'))

print(jsonobj['people'][1])
