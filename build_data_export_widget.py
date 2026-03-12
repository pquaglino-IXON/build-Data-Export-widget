import json

with (open("data-tags.csv", "r")) as csvFile:
    csv = csvFile.readlines()

tags = []
for line in csv:
    split = line.split(',')
    # Include tags sampled on interval only
    if split[7] == "interval":
        tags.append(split[0])

inputs = {
   "header":{
      "title":"Download",
      "subtitle":"Download all data"
   },
   "input":{
      "metrics":[
      ],
      "export":{
         "fileName":"test",
         "fileFormat":"csv:comma",
         "buttonName":"Export"
      }
   }
}

for tag in tags:
    tagObj = {
            "tag":{
               "heading":f"{tag}",
               "metric":{
                  "selector":f"Agent#selected:data-source.tag.{tag}",
                  "decimals":None,
                  "unit":None,
                  "factor":None
               }
            }
         }
    inputs["input"]["metrics"].append(tagObj)
j_inputs = json.dumps(inputs)
widget = {
   "template":{
      "publicId":"3XLN3AVrJqxe",
      "reference":{
         "name":"PageComponentTemplate"
      }
   },
   "inputs":f"{j_inputs}",
   "dimensions":{
      "type":"sheet",
      "left":0,
      "top":14,
      "cols":2,
      "rows":3,
      "mobileHeight":None,
      "mobileOrder":None,
      "mobileLeft":None,
      "mobileCols":None
   }
}
with (open("output.json", "w") as output):
    output.write(json.dumps(widget, indent=4))

print("Done.")

