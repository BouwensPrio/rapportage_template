Draai dit bij voorkeur in een virtual environment
'''
PS> py -m venv venv\
PS> venv\Scripts\activate
PS> pip install -r requirements.txt
'''

Kies vervolgens het sjabloon bestand en draai het script

'''
PS> python process_template.py basis_priocura_productie_v2.3.docx
'''

basis_priocura_productie_v2.3.docx bevat mogelijkheid voor inklappen toelichting
basis_priocura_productie_v2.3.docx bevat die mogelijkheid niet, verder gelijk

Aangemaakte sjablonen zijn vervolgens te vinden in de map /Sjablonen

Invulling voor de sjablonen komt tot stand vanuit basic_structures.py

basic_structures.py bevat:
diverse Lists
diverse Dictionaries

def get_report():
Bevat een List of Lists, iedere List bevat een opbouw van sjablonen. 
De sjablonen worden gemerged in volgorde links --> rechts door
def merge_list():
bevat een algoritme voor het (deels) mergen van een geneste Dict
def merge():
is een helper-functie

Elementen schuiven min of meer in elkaar van links naar rechts
Bestaande elementen blijven bestaan, kunnen alleen worden uitgebreid of worden vervangen
Zo is het mogelijk om een hiërarchie met aftakkingen van sjablonen te maken


