# Morning Sunshine

Ce programme vise à déterminer les bénéfices potentiels en augmentant de 5% le loyer des appartements qui font face au lever du soleil.

## Contexte et problématique

Un promoteur immobilier possède une route avec tous les bâtiments s'y trouvant. Voulant faire des bénéfices, connaissant les informations suivantes:

-   Les batiments sont orientés sur l'axe Ouest-Est,
-   les batiments ont des appartements qui peuvent être orientés ou non vers L'Est (possibilité de voir le levé du soleil),
-   les clients considèrent comme un plus le fait d'avoir un appartement faisant face au soliel levant;

Le commité de direction souhaiterait donc savoir quels bénéfices peuvent être réalisés en augmentant de 5% le loyer des appartements concernés pour l'année à venir.

## Présentation du code

La logique du programme est implémentée dans une fonction appelée `benefits_prediction` qui calcule les bénéfices annuels des loyers en fonction de l'orientation des appartements.

La boucle principale du programme parcoure l'ensemble des bâtiments, de nombre `n` et pour chaque bâtiment il parcoure l'ensemble des appartements dont le nombre sera noté `m` pour extraire dans une liste les appartements pouvant rapporter un bénéfice ; et enfin parcoure cette dernière liste, de taille `l`, pour calculer ces bénéfices.

```
O(n * (m + l))
```

Le programme reçois en argument une liste de batiments sous format JSON converti en chaine de caractères:

```json
[
	{
		"height": 15,
		"floor_layout": [
			{ "monthly_rent": 1200, "orientations": ["E", "N"] },
			{ "monthly_rent": 1200, "orientations": ["S", "W"] }
		]
	},
	{
		"height": 6,
		"floor_layout": [
			{ "monthly_rent": 2300, "orientations": ["N", "S", "E", "W"] }
		]
	}
]
```

-   La fonction itère alors sur la liste de bâtiment dans l'ordre inverse en commençant par le dernier bâtiment. Pour chaque bâtiment, elle récupère la hauteur et les informations de disposition des étages.

-   Ensuite elle identifie les appartements faisant face au soleil levant (ayant une orientation vers l'est) et ayant une hauteur supérieur aux tailles des bâtiments précédemment traités.

-   A partir de là, `benefits_prediction` calcule les bénéfices mensuels par appartement, pour ensuite les multiplier par 12 (le nombre de mois dans l'année) et par le nombre d'appartement profitant du levant dans le batiment.

Les bénéfices calculés représentent l'augmentation potentielle des revenus pour le promoteur immobilier si le loyer des appartements faisant face au lever du soleil est augmenté de 5% pour l'année à venir.

## Utilisation

Pour utiliser le code, vous devez fournir une représentation JSON valide des bâtiments en tant qu'argument de ligne de commande. Le JSON doit suivre un format spécifique.

Voici un exemple de commande pour exécuter le code :

```bash
python morning_sunshine.py "[{\"height\": 15,\"floor_layout\": [{ \"monthly_rent\": 1200, \"orientations\": [\"E\", \"N\"] },{ \"monthly_rent\": 1200, \"orientations\": [\"S\", \"W\"] }]},{\"height\": 6,\"floor_layout\": [{ \"monthly_rent\": 2300, \"orientations\": [\"N\", \"S\", \"E\", \"W\"] }]}]"
```

---

## Contributeurs:

    dossa_d
    qasmi_m
    gueye_d
