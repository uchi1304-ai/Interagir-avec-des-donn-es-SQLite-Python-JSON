fetch("produits_complet.json")
  .then(res => res.json())
  .then(data => {
    afficherProduits(data.produits);
    afficherRupture(data.rupture);
    afficherValeurCategorie(data.valeurparcategorie);
    afficherValeurTotale(data.valeurtotalestock);
  });

  function afficherProduits(produits) {
  const liste = document.querySelector("#liste-produits");
  liste.innerHTML = "";
  produits.forEach(p => {
    const li = document.createElement("li");
    li.textContent = `${p.nom} — ${p.prix}€ — Stock: ${p.stock}`;
    liste.appendChild(li);
  });
}

  function afficherRupture(rupture) {
  const liste = document.querySelector("#rupture");
  liste.innerHTML = "";
  rupture.forEach(p => {
    const li = document.createElement("li");
    li.textContent = `${p.nom} — ${p.prix}€ — Stock: ${p.stock}`;
    liste.appendChild(li);
  });
}

 function afficherValeurCategorie(valeurs) {
  const liste = document.querySelector("#valeur-categorie");
  liste.innerHTML = "";
  valeurs.forEach(p => {
    const li = document.createElement("p");
    li.textContent = `${p.categorie} — ${p.valeur_par_categorie}€`;
    liste.appendChild(li);
  });
}


 function afficherValeurTotale(total) {
  const liste = document.querySelector("#valeur-totale");
  liste.innerHTML = "";
  total.forEach(p => {
    const li = document.createElement("p");
    li.textContent = `${p.valeur_total_stock}€`;
    liste.appendChild(li);
  });
}


