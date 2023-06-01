# Tweety one Pilots

Ce programme Affiche les `#hashtags` les plus utilisés sur Twitter en fonction d'un ensemble de données contenues dans un fichier dans le format JSON.

## Contexte & problématique

Danss le bût de connaitre les sujets qui intéressent le plus les utilisateurs de Twitter, notre entreprise rescence dans un fichier json, les twits postés sur Twitter une période donnée.

## Code: présentation & complexité

La logique du programme a été implémentée dans une fonction nomée `most_used_hashtags` qui va extraire dans une liste les hashtags se trouvant dans le fichier ainsi que leurs occurances.

Le programme reçoit en entrée le chemin absolue ou relatif de fichier JSON.

-   De ce fichier il extrait la liste des tweets sur une période donnée,

-   Ensuite il itère sur la list récupérée pour en extraire les hashtags dans uns liste temporaire.

-   Cette liste sera retriée de celui ayant le plus d'occurences à celui ayant le moins et tous les doublons sont retirés.

-   Et pour finir, cette liste est affichée sous format d'une liste JSON.

La liste affichée représente alors les hashtags les plus utilisés sur une période donnée, de la plus utilisée à la moins utilisée.

Soient `n` le nombre de tweets/hashtags contenu dans le fichier:

```
# La complexité serait:
O(n + n + n + n + n + n + n)
# ou
O(7n)

# d'où
O(n)
```

## Utilisation

Pour utiliser ce programme, vous devez fournir le chemin absolu ou relatif du fichier json contenant les informations necessaire en tant qu'argument de ligne de commande.

Voici un exemple de commande pour exécuter le code :

```bash
python tweety_one_pilots.py ./tweets.json
```

---

## Contributeurs:

    dossa_d
    qasmi_m
    gueye_d
