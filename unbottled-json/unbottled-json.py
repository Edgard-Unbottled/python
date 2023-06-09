import pandas as pd
import json
import os

# Lire le fichier Excel
xl_file = pd.ExcelFile('C:/Users/edgar/Documents/dev/sandbox/pdp/unbottled_deo_ingredient.xlsx')

# Parcourir chaque feuille
for sheet_name in xl_file.sheet_names:
    # Charger les données de la feuille dans un DataFrame
    df = xl_file.parse(sheet_name)

    # Convertir les données en dictionnaire
    data_dict = df.to_dict('records')

    # Créer le dictionnaire final avec les clés "ingredients" et "nom_onglet"
    final_dict = {"ingredients": data_dict}

    # Convertir le dictionnaire en JSON
    json_data = json.dumps(final_dict, indent=4, ensure_ascii=False)

    # Créer le dossier 'result-json' s'il n'existe pas déjà
    if not os.path.exists('result-json'):
        os.mkdir('result-json')

    # Écrire le JSON dans un fichier avec le nom de l'onglet actuel dans le dossier 'result-json'
    with open(f'result-json/{sheet_name}.json', 'w', encoding='utf-8') as f:
        f.write(json_data)
