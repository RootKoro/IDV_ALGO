# Pattern particulier

Ce programme recherche dans les fichiers demandés, des chaines de caractères précises ; pour ensuite afficher les chaines de caractères avec leurs positions et leurs fichiers d'appartenance.

---

## Contexte & problématique

Pour permettre la recherche de chaines de caractères dans de gros volumes de données, nous aurions besoin d'un outil de recherche rapide permettant non seulement de trouver la chaine de caractères à chercher, mais aussi sa position dans les volumes de données.

## Code: présentation & complexité

La logique de cette outille a été développé dans une fonction nomée `search_pattern` qui stoque temporairement le contenu de chaque fichier, un à un, pour ensuite rechercher, dans le contenu récupéré, la chaine de caractères à trouver, toutes ses occurences ainsi que ses positions avant de passer au fichier suivant, s'il y en a.

Le programme reçoit en entré, en ligne de commande, tous les `patterns` (chaines de caractères) à chercher ainsi que les chemins (absolus / relatifs) des ficheirs dans lesquels se passeront la recherche de ces patterns.

-   Il remplira deux listes, une qui contiendra l'ensemble des patterns à chercher ; et l'autre l'ensemble des fichiers dans lesquels les patterns seront recherchés ;

-   Pour évirter une surutilisation des resources, le programme parcourera les fichiers un à un pour chercher chaque pattern, les occurences et positions dans le fichier (procéder P0) ;

-   Une autre alternantive serai de chercher les occurences de chaque pattern et leurs positions en procédant pattern par pattern au lieu de procéder fichier par fichier; mais ce procéder est plus lent (procéder P1).

Soient `n` le nombre de fichiers à parcourir, `m` le nombre de patterns à chercher et `k` le nombre d'occurence d'un pattern dans un seul fichier:

```
O(n * m * k)
# complexité cubique
```

## Utilisation

Pour utiliser ce programme, vous devez fournir le chemin absolu ou relatif des fichiers dqns lesquels les patterns doivent être chercher ainsi que les patterns à chercher précédés de `'-e'` en tant qu'argument de ligne de commande.

Voici un exemple de commande pour exécuter le code :

```bash
python pattern_particulier.py -e dolor -e volupta lipsum.txt
```

---

## Contributeurs:

    dossa_d
    qasmi_m
    gueye_d
