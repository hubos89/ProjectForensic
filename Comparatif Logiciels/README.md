# Test de récupération de données en fonction du temps

Nous avons voulu voir quel logiciel était le plus rapide et le plus efficace. 

Le protocole est le suivant : 

- Utilisation d'un ordinateur dont le disque dur a été effacé
Pour ce cas, nous avons pris 2 ordinateurs. Le premier a été testé via une clé bootable sous Linux et le deuxième via son installation Windows. 

- Utilisation d'un logiciel (Linux / Windows) pour récupérer les données. 

Dans un premier temps nous avons choisi les différents logiciels via une recherche internet pour connaître les alternatives à Foremost. 
Les logiciels retenus sont les suivants : 

* PhotoRec (Linux & Windows) 
* GNU ddrescue (Linux)
* TestDisk (Linux & Windows)
* Recuva (Windows)

Dans un second temps nous avons réalisé le protocole établi ci-dessus. Nous obtenu les résultats ci-dessous.
### Aperçu final des différentes solutions

###### Foremost : 
Utilisation basique du script vu dans les sous-parties différentes de notre git.
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/foremost_final.png "Aperçu Final Foremost")

###### [PhotoRec](https://www.cgsecurity.org/wiki/PhotoRec) :
Logiciel libre qui se présente sous la forme de lignes de commande. Plus complet que Foremost et permet de passer qu'une seule fois dans le disque dur au lieu de plusieurs passages comme expliqué dans les autres sous-parties. Il peut être utilisé sous Windows et Linux.
Sous Linux ou Windows, les dossiers se présentent de la même manière :
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/photorec_final.PNG "Aperçu Final Photorec")

De plus, voici le traitement sous Windows : 
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/photorec_win.png "Aperçu Final Photorec")

###### [GNU ddrescue](https://www.linux.com/learn/intro-to-linux/2017/3/GNU-DDRESCUE-BEST-DAMAGED-DRIVE-RESCUE) :
Malheureusement, malgré avoir suivi plusieurs tutoriels aucune donnée n'a réussi à être extraite au bout d'une heure. De nombreuses erreurs sont apparues comme par exemple le fait que le disque dur externe ne correspond pas aux attentes de GNU ddrescue.

###### [TestDisk](https://www.cgsecurity.org/wiki/TestDisk):
Malheureusement, malgré avoir suivi plusieurs tutoriels aucunes données n'a réussi à être extraite au bout d'une heure sur Linux et Windows. Comme-ci-dessus, après de nombeux formatage du disque dur externe, aucune donnée n'a pu être extraite. 

###### [Recuva](https://www.ccleaner.com/recuva):
Logiciel gratuit développé par Piriform (tout comme CCleaner) permet de restaurer, via Windows, des fichiers marqués par le système comme "libres" et donc sous-entendu comme "supprimés".
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/recuva_final.png "Aperçu Final Recuva")

Ici nous pouvons voir une restauration des fichiers en cours : 
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/recuva_recover.png "Aperçu d'une restauration Recuva")

###### [The Sleuth Kit (TSK)](https://www.sleuthkit.org):

Le *framework* **The sleuth kit** n'est plus en développement et il est préférable d'utiliser **Autopsy**. Cependant, nous avons pris la peine de nous renseigner sur cette bibliothèque qui peut toujours être utilisée.

Le principe de ce *framework* se passe en trois étapes et permet de récupérer des fichiers sur un disque dur comme **Foremost** le ferait : 

1. Il y a une récupération des méta-données et qui sont centralisées dans une base de données (SQLite, MySQL...) ;
2. Il y a un rajout d'effectué dans cette BDD des informations comme la valeur des hashs, de l'entropie... ;
3. On regroupe toutes les informations dans un document.

**TSK** peut être utilisé en ligne de commande ou sur un programme en C++. En consultant la documentation nous pouvons lire que des fonctions existent pour accéder aux contenus des fichiers sur les disques.

###### [Autopsy](https://www.sleuthkit.org/autopsy/):

Autopsy utilise les commandes de TSK et utilise une interface graphique via un client web.
La phase préparatoire permet d'indiquer le nom de la BDD qui va être utilisée, le nom des personnes travaillant sur le projet et un calcul du hash s'effectue après avoir indiqué sur quelle image nous travaillons.

Une fois le calcul effectué sur l'intégralité du disque, nous pouvons explorer celui-ci, voir les hashs des fichiers et lire les contenus.

![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/Autopsy.png "Aperçu de l'interface d'Autopsy avec une récupération")


### Récapitulatif des résultats obtenus

Voici le tableau récapitulatif de nos résulats en prenant en compte seulement le temps et la quantité de données récupérées :

| Solution      | Ordinateur|Temps estimé | Temps réalisé   | Quantité de données | Nombre de fichiers  |Nombre de secteurs lus|
| ------------- |:---------:|:-----------:|:---------------:|:-------------------:|:-------------------:|:--------------------:|
| Foremost      |  1        |  ???        | > 2j            | > 36 Go             |  > 500 000          |625 142 448           |
| PhotoRec      |  1        | > 150h      | 1h              | > 4 Go              | 8263                |10 507 792            |
| PhotoRec      |      2    | > 51h       | 1h              | > 10 Go             | > 72 000            |624 932 864           |
| GNU ddrescue  |  1        | > 2h        | 1h              | ????                |        ????         |              ????    |
| TestDisk      |      2    | > 1h        | 1h              | ????                |        ????         |       624 932 864    |
| Recuva        |  2        | > 2h        | 1h 51m 44s      | > 80 Go (20Go extrait) |  1 177 043       |       624 932 864    |

  
Voici le tableau récapitulatif de nos résulats en prenant en compte cette fois le nombre de fichiers en fonction de leurs types :

#### Linux

| Solution      | DOC, TXT    | GIF    | JPG    | PDF    |PNG     | PPT(x) |XLS     |ZIP     | WAV, ... | EXE    |
| ------------- |:-----------:|:------:|:------:|:------:|:------:|:------:|:------:|:------:|:--------:|:------:|
| Foremost      | > 2000      | 105 326| 54 469 | 27 604 | 272 848| > 500  | 1361   | 9595   | > 150    |  ???   |
| PhotoRec	    | 4719	      | 232    |	329	  | ???    |	1241	| ???	   | ???	  | ????   |	>150	  | 1386   |


#### Windows
| Solution      | TXT   | EXE    | PNG  | ZIP  | TTF | BMP |RIFF  |JPG    | AUTRES | 
| ------------- |:-----:|:------:|:----:|:----:|:---:|:---:|:----:|:-----:|:------:|
| PhotoRec      | 35 312| 29 539 | 2554 | 857  | 734 | 541 | 458  | 376   | > 2000 |

| Solution      | APPLICATION  | ARCHIVE  | CATALOGUE SECU | TXT |EXT APP | XLS |PNG   |Autres    |
| ------------- |:------------:|:--------:|:--------------:|:---:|:------:|:---:|:----:|:--------:|
| Recuva        | 547          |  271     |  2955          | 840 | 3156   | 58  | 4099 | > 20 000 |
