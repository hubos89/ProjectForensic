## Analyse post récupération

Le fichier VirusTotalAll permet d'analyser un dossier (passé en parametre) en recherchant les hash des fichiers du dossier sur virustotal. Cela permet de faire une recherche virale simple mais sans envoyer de fichiers contenant des informations sensibles puisque seulement les hash sont envoyés. 

Le programme parcourt tout les fichiers inclu dans le dossier ainsi que les sous dossiers passé en parametre. Ensuite pour chacun d'eux, il va créer le hash MD5 du fichier puis envoyer la requete a VirusTotal pour faire une recherche dans leur base de donnée. Une fois la réponse reçut, si le résultat est positif, le résultat de l'analyse est ecrit dans un fichier au nom du fichier dans un dossier spécial.

![Résultat par fichier](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/TestVirusTotalRes.PNG)

De plus, dans un autre fichier coresponsant à l'analyse, le nom du fichier positif est écrit. ainsi que le total de fichier positif sur le nombre de fihcier analysé

![Ficheir de résultat général](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/TestVirusTotal.PNG)

Le script pocède une fonction d'attente si le quota journalier sur l'API VirusTotal est atteint.

Il faut spécifier votre clé public virusTotal dans le code source
