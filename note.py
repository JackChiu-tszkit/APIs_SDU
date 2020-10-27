table = []
temp = []
with open("query.json", "r", encoding="utf8") as fd:
    data= json.load(fd)
fd.close()

#print(data.get('results'))
data1=data.get('results')
data1=data1[0]
print(len(data["results"]))

for i in range(len(data["results"])):
    file_path = "usr/jackchiu/output/table" + str(i) + ".csv"
    with open(file_path, "w", newline="") as fd:
        writer = csv.writer(fd)
        for row in data["tables"][i]["data"]:
            temp.clear()
            for element in row:
                temp.append(element["text"])
            writer.writerow(temp)
            # table.append(temp)
        # pprint.pprint(table)
    fd.close()
