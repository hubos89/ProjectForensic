# Traitement avec Foremost

Nous avons choisi comme solution de récupération principale foremost. C'est un outil disponible de base sur Kali Linux et qui a répondu à nos attentes.

Le seul défaut de cet outil réside dans le fait que son processus s'arrête de manière aléatoire et nous n'avons guère réussi à en trouver la cause. Pour pallier ce problème, nous avons écrit un script qui récupère le type de fichier en fonction du document analyser lors du processus. L'ensemble des actions est beacuoup plus lente mais chaque étape de manière individuelle est plus courte que de lancer un Foremost global. Grâce à cette technique nous n'avons eu aucune interruption lors de nos tests mais cela a rallongé considérablement la durée de récupération des données. 

Nous avons préféré avoir un résultat optimal et fiable plutôt que de devoir recommencer certaines actions en boucle sans visuel. 

Le script doit être lancé avec les droits root tout comme foremost pour pouvoir fonctionner. Le seul paramètre à donner est le chemin d'accès du dossier de destination. Le script s'occupe d'extraire les données du disque SDA et les place de façon triées dans le dossier placé en paramètre.
![Foremost](https://github.com/hubos89/ProjectForensic/blob/master/Traitement%20de%20Base%20avec%20foremost/foremost.png)

L'avancement du processus n'est pas affiché dans la console car foremost affiche enormément d'informations, il est donc écrit dans un fichier texte dans le dossier de destination appelé *avance.txt*. Chaque type de fichier récupéré y est écrit au fur et à mesure de l'avancement du procéssus. 

![Foremost](https://github.com/hubos89/ProjectForensic/blob/master/Traitement%20de%20Base%20avec%20foremost/foremostAvance.png)
