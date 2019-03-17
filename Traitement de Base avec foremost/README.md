# Traitement avec Foremost

Nous avons choisi comme solution de récupération principale foremost. C'est un outil disponible de base sur Kali Linux et qui a répondu à nos attentes.

Le seul défaut de cet outil réside dans le fait que son processus s'arrête de manière aléatoire et nous n'avons guère réussi à en trouver la cause. Pour pallier ce problème, nous avons écrit un script qui récupère le type de fichier en fonction du document analyser lors du processus. L'ensemble des actions est beacuoup plus lente mais chaque étape de manière individuelle est plus courte que de lancer un Foremost global. Grâce à cette technique nous n'avons eu aucune interruption lors de nos tests mais cela a rallongé considérablement la durée de récupération des données. 

Nous avons préféré avoir un résultat optimal et fiable plutôt que de devoir recommencer certaines actions en boucle sans visuel. 
