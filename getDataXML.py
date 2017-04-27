import requests
import datetime
from lxml import etree
import json

def getValue(topic):
    if topic == "direccion" or topic == "velocidad":
        return forecast.xpath("//viento[@periodo=\"" + str(hour).zfill(2) + "\"]/"+topic+"/text()")[moment]
    else:
        return int(forecast.xpath("//"+topic+"[@periodo=\""+str(hour).zfill(2)+"\"]/text()")[moment])

locality = 28079 #Madrid
hour = 20 #0 - 23
moment = 0 #0: present, 1: future
data = {}

xml = requests.get("http://www.aemet.es/xml/municipios_h/localidad_h_"+str(locality)+".xml").content
forecast = etree.XML(xml)

data["DayName"] = datetime.datetime.now().strftime("%A")
data["Temperature"] = getValue("temperatura")
data["WindChill"] = getValue("sens_termica")
data["RH"] = getValue("humedad_relativa")
data["Rainfall"] = getValue("precipitacion")
data["WindDirection"] = getValue("direccion")
data["WindSpeed"] = int(getValue("velocidad"))

j = json.dumps(data)
print(j)
