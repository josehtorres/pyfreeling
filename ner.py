from lxml import etree
from pyfreeling import Analyzer

config_file = '/usr/share/freeling/config/es.cfg'

#text = """La canasta de consumo para un hogar compuesto por un matrimonio con dos hijos e inquilinos de la vivienda. """

text = "buen dia Previser, habla Maria Eugenia en que le puedo orientar gracias, habla con Margot Acosta, necesito un servicio de Pediatria"
#Pediatria, si es posible con el doctor Rodrigo Palacios, en la Clinica Tequendama de la ciudad de Cali o con el doctor Santiago Cucalon, del #Centro Medico Imbanaco de la ciudad de Medellin o Palmira."

analyzer = Analyzer(config=config_file, lang='es')
output = analyzer.run(text, 'flush')

print(etree.tostring(output))
