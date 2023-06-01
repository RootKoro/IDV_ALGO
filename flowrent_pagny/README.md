# Flowrent Pagny

Affiche une simulation simple d'un workflow ou d'un ensemble de workflow, en affichant l'équivalent hexadécimal du hachage md5 correspondant à l'exécution de l'ensemble de ses tâches.

---

## Contexte & problématique

Afin d'améliorer la productivité de notre entreprise, il faudrait songer à automatiser les processus récurrents. Dans ce sens, notre entreprise nous a demandé de développé un programme permettant de simuler l'exécution des processus de traitements de données.

## Code: présentation & complexité

Ce programme a été développé dans une classe nommée `WorkFlowSimulation` contenant les attributs et méthodes nécessaires pour le bon fonctionnement du programme.

Le programme reçoit en entrée, en ligne de commande, deux listes, une première liste de tâches et une seconde liste de workflows.

-   Il crée d'abord une instance de la classe `WorkFlowSimulation` avec les listes reçues en arguments ;

-   De cet instance il appelle la méthode `workFlowSimulation` qui pertmet de remplir l'attribut `simulatedWorkflows` qui est une liste des résultats des simulations de chaque workflow en itérant sur la liste workflos à exécuter ainsi que sur la liste des tâches à exécuter dans chaque workflow ;

-   Et pour finir il affiche sous format JSON la liste des résultats obtenus

Soit `n` le nombre total de workflow, `m` le nombre total de tâches, `l`le nombre de tâches par workflow, `k` ; la complexité serait :

```
O(n * k * m * n)
```

## Utilisation

Pour utiliser ce programme, vous devez en tant qu'argument de ligne de commande deux listes en formats JSON, en commançant d'abord par la liste des tâches et ensuite par la liste des workflows.

Voici un exemple de commande pour exécuter le code :

```bash
python flowrent_pagny.py "[{\"id\": 0, \"task_type\": \"primitive\"}, {\"id\": 1, \"tasks\": [0], \"task_type\": \"workflow\"}]" "[{\"workflow_id\": 1, \"input\": \"Ma liberté de penser\"}]"
```

---

## Contributeurs:

    dossa_d
    qasmi_m
    gueye_d
