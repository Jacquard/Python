#!/usr/bin/env python3

import urllib.request
import re

print("")
url = input("URL?		")
#url="http://www.lasexta.com/programas/el-objetivo/noticias/entrevista-completa-edward-snowden-objetivo-version-extendida_2016031300159.html"
pagina1 = urllib.request.urlopen(url).read()
cadena_desc = re.findall('http://www.lasexta.com/videosnuevosxml/[0-9]*/[0-9]*/[0-9]*/[0-9]*/[0-9]*/[0-9]*/[0-9]*.xml',pagina1.decode("utf-8", "ignore"))[0]

pagina2 = urllib.request.urlopen(cadena_desc).read()
final = re.findall('http://deslasexta.antena3.com/mp_series2/[0-9]*/[0-9]*/[0-9]*/[0-9]*.mp4',pagina2.decode("utf-8", "ignore"))[0]

print("URL video:	",final)
print("")
