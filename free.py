# -*- coding: utf-8 -*-
from lxml import etree
from pyfreeling import Analyzer
#import os
#import pandas as pd

#os.chdir("/home/jose")
#text = pd.read_csv('llamada.txt')

#text = "buen dia Previser, habla Maria Eugenia en que le puedo orientar gracias, habla con Margot Acosta, señorita necesito un servicio de Pediatria, si es posible con el doctor Rodrigo Palacios, en la Clinica Tequendama de la ciudad de Cali o con el doctor Santiago Cucalon, del Centro Medico Imbanaco de la ciudad de Medellin o Palmira, para el dia 23 de marzo de 2019"

texto = open('llamada.txt', 'r') 
text = texto.read()


analyzer = Analyzer(config='es.cfg', lang='es')

output = analyzer.run(text, 'ner', outlv='tagged')
texto.close()

Ner = etree.tostring(output)
#print (Ner)

archivo = open('llamadaNer.jht', 'w') 
Ner = str(Ner)
archivo.write(Ner)
archivo.close()




#with open("Ner.txt", 'w') as f:
#for line in f:
#	if "ORG" in line:
#	print 'line'
#	if "PER" in line:
#	print line
#	if "LOC" in line:
#	print line



#text = open('/home/jose/llamada.txt', mode='r', encoding='utf-8')


