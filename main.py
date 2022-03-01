import matplotlib.pyplot as plt
import pandas as pd

with open('RealisationDonneesProduction_2021.xls', mode="r", encoding="latin-1") as file:
    df = file.read().split('Données')
    df = [i.split("\n") for i in df]
    df = [[j.split("\t") for j in i] for i in df]

# ['Heures', 'Biomasse', 'Gaz', 'Charbon', 'Fioul', 'Hydraulique STEP', "Hydraulique fil de l'eau / éclusée", 'Hydraulique lacs', 'Nucléaire', 'Solaire', 'Déchets', 'Éolien terrestre', 'Total', '']
print(df)
