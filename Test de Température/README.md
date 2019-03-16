## Test de récupération de données en fonction de la température

Nous avons voulut voir si la température avait un impact sur la récupération de fichier. 

Nous avons donc mis au point un protocol simple : lancer des tests avec foremost avec un timeout de 10 minutes afin de comparer les résultats en fonction de la température.
```bash 
timeout 10m foremost -i /dev/sda -o /media/root/******/testTemp1 
```
La température de la pièce été de 22 degrès et l'ordinateur sera placé devant un four afin de faire monter progréssivement la température du disque dur.
les relevé de température ont été éffectué avec la commande hddtemp au début et a la fin du foremost.

Nous nous sommes arrété a 90° pour ne pas endomager le matériel.



| Température   | Nombre de fichier  | Quantité de Donnée  |
| ------------- |:------------------:| -------------------:|
| 43°-47°       | 46474              | 3.6Go               |
| 64°-70°       | 46036              | 3.58Go              |
| 73°-76°       | 45944              | 3.58Go              |
| 81°-91°       | 42918              | 3.41Go              |

![Graphique](https://github.com/hubos89/ProjectForensic/blob/master/Test%20de%20Temp%C3%A9rature/GraphTemperature.png "Nombre de Fichier et Quantitées de données en fonction de la température")


Comme on peut le constater sur les différent graphiques, la température a un impact léger sur la récupération de données en dessous de 80°. Au dela de cette température on observe une baisse de 7% de la performance sur une dizaine de degrès en plus ce qui est moins négligeable. Cependant ces température son assez proche des condition maximale d'utilisation de matériel informatique (100° environt), la chute de performance est donc compréhensible arrivé à cette temérature. 
