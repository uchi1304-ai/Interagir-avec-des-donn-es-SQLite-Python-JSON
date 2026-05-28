import sqlite3
import json

# Connexion à la base
conn = sqlite3.connect("produit.db")
cur = conn.cursor()

# Exécuter une requête
cur.execute("SELECT * FROM produits")
rows= cur.fetchall()

# Récupérer les noms de colonnes
colonnes = [desc[0] for desc in cur.description]

# Transformer en dictionnaires
produits = []

for ligne in rows:
    produits.append(dict(zip(colonnes, ligne)))

    
# Exécuter une deuxieme requête (produits en rupture)
# Connexion à la base
cur.execute("SELECT nom, categorie, prix, stock FROM produits WHERE stock = 0")
rows= cur.fetchall()

# Récupérer les noms de colonnes
colonnes = [desc[0] for desc in cur.description]

# Transformer en dictionnaires
rupture = []

for ligne in rows:
    rupture.append(dict(zip(colonnes, ligne)))

# Exécuter une troisieme requête (valeur marchande totale par catégorie)
cur.execute("SELECT categorie,SUM(prix * stock) as valeur_par_categorie FROM produits GROUP BY categorie;")
rows= cur.fetchall()

# Récupérer les noms de colonnes
colonnes = [desc[0] for desc in cur.description]

# Transformer en dictionnaires
valeur_par_categorie = []

for ligne in rows:
    valeur_par_categorie.append(dict(zip(colonnes, ligne)))

# Exécuter une quatrieme requête (valeur totale du stock)
# Connexion à la base

cur.execute("SELECT *,SUM(prix * stock) AS valeur_total_stock FROM produits")
rows= cur.fetchall()

# Récupérer les noms de colonnes
colonnes = [desc[0] for desc in cur.description]

# Transformer en dictionnaires
valeur_totale_stock= []

for ligne in rows:
    valeur_totale_stock.append(dict(zip(colonnes, ligne)))


# Créer le JSON complet
data = {
 "produits": produits,
 "rupture": rupture,
 "valeurparcategorie": valeur_par_categorie,
 "valeurtotalestock": valeur_totale_stock
}

with open("produits_complet.json", "w", encoding="utf-8") as f:
 json.dump(data, f, indent=4, ensure_ascii=False)

conn.close()

print("Export complet terminé.")







