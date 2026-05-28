import sqlite3
import json
#Connexion à la base
conn = sqlite3.connect("produit.db")
cur = conn.cursor()
# Exécuter une requête
cur.execute("SELECT * FROM produits")
rows = cur.fetchall()
# Récupérer les noms de colonnes
colonnes = [desc[0] for desc in cur.description]

#Transformer en dictionnaires
donnees = []
for ligne in rows:
    donnees.append(dict(zip(colonnes, ligne)))

with open("produits.json", "w", encoding="utf-8") as f:
    json.dump(donnees, f, indent=4, ensure_ascii=False)

conn.close()

print("Export terminé.")

