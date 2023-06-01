# School's out

Ce programme détermine le nombre de classe minimum qu'il faut pour une journée d'école en fonction des sessions d'activités.

---

## Contexte & problématique

Une école souhaite optimiser la gestion/ l'allocation des salles en fonction des sessions d'activités qu'elle propose. Pour se faire elle a besoin d'un outil qui lui permettrait de calculer le nombre minimum de salle qu'il lui faudrait en fonction de l'ensemble des créneaux horaires des sessions qui se dérouleront dans la journée.

## Code: présentation & compléxité

Notre logique a été implémentée dans la fonction `minimum_classrooms` qui stocke temporairement le contenu du fichier contenant l'ensemble des sessions et les informations les concernants, pour ensuite calculer et retourner le nombre minimium de salles qu'il faudra.

Le programme reçoit en entrée, en ligne de commande, le chemin (absolu ou relatif) du fichier JSON contenant les informations sur une journée d'activités.

-   À partir de ce fichier, il extrait toutes les sessions d'activités dans une liste;

-   Il va ensuite itérer sur la liste et créer une liste intermédiaire contenant les sessions précédentes à la session sur laquelle se trouve la boucle principale;

-   Puis il va comparer les sessions précédentes à la session actuelle pour déterminer combien de sessions se tiendront simultannément à la session sur laquelle se trouve la boucle principale;

-   Et enfin il va comparer le nombre de sessions se tenant en simultané et le nombre minimum de salles à alloué pour incrémenter ce dernier si il y a plus de sessions en simultané que de classe disponible.

Soit n le nombre de sessions se trouvant dans le fichier; sachant que le programme boucle principalement sur n, pour ensuite boucle sur 2 -> n - 1, la complexité est donc de:

```
O(n!)
# complexité factorielle
```

## Utilisation

Pour utiliser ce programme, vous devez fournir le chemin absolu ou relatif du fichier JSON contenant l'ensemble des sessions d'activités d'une journée en tant qu'argument de ligne de commande.

Voici un exemple de commande pour exécuter le code :

```bash
python schools_out.py sessions.json
```

---

## Contributeurs:

    dossa_d
    qasmi_m
    gueye_d
