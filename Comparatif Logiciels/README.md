# Test de récupération de données en fonction du temps

Nous avons voulu voir quel logiciel était le plus rapide et le plus efficace. 

Le protocole est le suivant : 

- Utilisation d'un même ordinateur pour toutes les solutions
- Utilisation de Foremost comme référence donc complétion de son processus jusqu'au bout du temps annoncé
- Utilisation des autres solutions avec seulement 1H pour échantillonnage

Dans un premier temps nous avons choisi les différents logiciels via une recherche internet pour connaître les alternatives à Foremost. 
Les logiciels retenus sont les suivants : 

* Photorec
* test
* test

Dans un second temps nous avons réalisé le protocole établi ci-dessus. Nous obtenu les résultats ci-dessous.
### Aperçu final des différentes solutions

###### Foremost : 
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/foremost_final.png "Aperçu Final Foremost")

###### Photorec :
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/photorec_final.png "Aperçu Final Photorec")

### Récapitulatif des résultats obtenus

Voici le tableau récapitulatif de nos résulats en prenant en compte seulement le temps et la quantité de données récupérées :

| Solution      | Temps estimé       | Temps réalisé       | Quantité de données | Nombre de fichiers  |Nombre de secteurs lus|
| ------------- |:------------------:|:-------------------:|:-------------------:|:-------------------:|:--------------------:|
| Foremost      |  ???               | > 2j                | > 36 GO             |  > 500 000          |625 142 448           |
| Photorec      | > 150h             | 1h                  | > 4 GO              | 8263                |10 507 792            |
| Photorec      | > 150h             | 1h                  | ????                |              |625142448             |
| Photorec      | > 150h             | 1h                  | ????                |           |625142448             |
  
Voici le tableau récapitulatif de nos résulats en prenant en compte cette fois le nombre de fichiers en fonction de leurs types :

| Solution      | DOC, TXT    | GIF    | JPG    | PDF    |PNG     | PPT(x) |XLS     |ZIP     | WAV, ... | EXE    |
| ------------- |:------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:-----------:|:------:|
| Foremost      | > 2000 | 105 326| 54 469 | 27 604 | 272 848| > 500  | 1361   | 9595   | > 150       |  ???   |
| Photorec      |  4719    | 232    | 329    |    ??? | 1241   |  ???   |  ???   |   ???? |  >150       | 1386   |
