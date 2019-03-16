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

Exemple de restauration sous Windows : 
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/photorec_win.png "Aperçu Windows Photorec")

###### [GNU ddrescue](https://www.linux.com/learn/intro-to-linux/2017/3/GNU-DDRESCUE-BEST-DAMAGED-DRIVE-RESCUE) :
Malheureusement, malgré avoir suivi plusieurs tutoriels aucune donnée n'a réussi à être extraite au bout d'une heure. De nombreuses erreurs sont apparues comme par exemple le fait que le disque dur externe ne correspond pas aux attentes de GNU ddrescue.

###### [TestDisk](https://www.cgsecurity.org/wiki/TestDisk):
Malheureusement, malgré avoir suivi plusieurs tutoriels aucunes données n'a réussi à être extraite au bout d'une heure sur Linux. Comme-ci-dessus, après de nombeux formatage du disque dur externe, aucune donnée n'a pu être extraite. Néanmoins, 
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/testdisk_win.png "Aperçu Final TestDisk")

###### [Recuva](https://www.ccleaner.com/recuva):
Logiciel gratuit développé par Piriform (tout comme CCleaner) permet de restaurer, via Windows, des fichiers marqués par le système comme "libres" et donc sous-entendu comme "supprimés".
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/recuva_final.png "Aperçu Final Recuva")

Ici nous pouvons voir une restauration des fichiers en cours : 
![alt text](https://github.com/hubos89/ProjectForensic/blob/master/Comparatif%20Logiciels/recuva_recover.png "Aperçu d'une restauration Recuva")


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
