## Analyse post récupération

Le fichier VirusTotalAll permet d'analyser un dossier (passé en parametre) en recherchant les hash des fichiers du dossier sur virustotal. Cela permet de faire une recherche virale simple mais sans envoyer de fichiers contenant des informations sensibles puisque seulement les hash sont envoyés. 

Le programme parcourt tout les fichiers inclu dans le dossier ainsi que les sous dossiers passé en parametre. Ensuite pour chacun d'eux, il va créer le hash MD5 du fichier puis envoyer la requete a VirusTotal pour faire une recherche dans leur base de donnée. Une fois la réponse recut, si le résultat est positif, le résultat de l'analyse est ecrit dans un fichier au nom du fichier dans un dossier spécial. De plus, dans un autre fichier coresponsant à l'analyse, le nom du fichier positif est écrit. 

Le script pocède une fonction d'attente si le quota journalier sur l'API VirusTotal est atteint.

Il faut spécifier votre clé public virusTotal dans le code source
