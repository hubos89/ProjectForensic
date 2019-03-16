## Test de récupération de données en fonction de la température

Nous avons voulu voir si la température avait un impact sur la récupération de fichier. 

Nous avons donc mis au point un protocol simple : lancer des tests avec Foremost avec un timeout de 10 minutes afin de comparer les résultats en fonction de la température.
```bash 
timeout 10m foremost -i /dev/sda -o /media/root/******/testTemp1 
```
La température de la pièce était de 22°C et l'ordinateur fut placé devant un four afin de faire monter progressivement la température du disque dur.
Les relevés de température ont été effectué avec la commande hddtemp au début et à la fin de la commande Foremost.

Nous nous sommes arrétés à 90°C pour ne pas endommager le matériel.



| Température   | Nombre de fichiers | Quantité de Données |
| ------------- |:------------------:| -------------------:|
| 43°C-47°C     | 46474              | 3.6Go               |
| 64°C-70°C     | 46036              | 3.58Go              |
| 73°C-76°C     | 45944              | 3.58Go              |
| 81°C-91°C     | 42918              | 3.41Go              |

![Graphique](https://github.com/hubos89/ProjectForensic/blob/master/Test%20de%20Temp%C3%A9rature/GraphTemperature.png "Nombre de Fichier et Quantitées de données en fonction de la température")
Comme on peut le constater sur le graphique ci-dessus, la température a un impact léger sur la récupération de données en dessous de 80°C. Au-delà de cette température, on observe une baisse de 7% de la performance sur la dizaine de degrés suivant cette limite, ce qui n'est pas négligeable. Cependant ces température sont assez proches des conditions maximales d'utilisation du matériel informatique (100°C environ), la chute des performances est donc compréhensible arrivé à ce stade. 
