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
