# Money for nothing

Ce programme permet de prédire les meilleurs dates d'achat et de vente de produits boursiers pour faire des bénéfices à court terme.

## Contexte et problématique

Un nouvel investisseur en bourse souhaiterait optimiser ses placements boursiers pour faire du profit à court terme.
Il dispose d'une liste de prédiction des prochains prix d'un produit boursier et voudrait connaitre les meilleurs dates d'achat et de revente pour un placement efficace de ses produits.

## Code: présentation et complexité

La logique de ce programme est principalement développée dans la fonction `bourse°predictor`. Elle parcour l'ensemble des predictions pour en retourner les plus pertinantes pour du profit à court terme.

Le programme reçoit en entrée, en ligne de commande, la liste des prédictions dans l'ordre des prix d'un produit boursier. Il parcour ensuite la liste pour trouver les meilleurs prix d'achat et de vente et retourne la liste contenant les indexes des meilleurs prix, les positions impaires correnspondantes aux indexes des meilleurs prix d'achat, et les positions paires, aux indexes des meilleurs prix de vente.

Soit `n` le nombre de prédiction à parcourir ; la complexité de ce programme ne dépendra que ddu facteur `n` étant donné le fait que le programme ne boucle que sur l'ensemble des prédictions.

```
O(n)
```

## Utilisation

Pour utiliser ce programme, vous devez fournir après l'appelle du programme une liste des prédictions des futures prix dans l'ordre d'un produit boursier en tant qu'argument de ligne de commande.

Voici un exemple de commande pour exécuter le code :

```bash
python money_for_nothing.py "[108, 45, 216, 215, 213, 96, 167, 245]"
```

---

## Contributeurs:

    dossa_d
    qasmi_m
    gueye_d
