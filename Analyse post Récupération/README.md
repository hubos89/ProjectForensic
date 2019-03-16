# Analyse post-récupération 

## Analyse Virale

Le fichier VirusTotalAll permet d'analyser un dossier (passé en paramètre) en recherchant les hashs des fichiers du dossier sur [VirusTotal](https://www.virustotal.com/). Cela permet de faire une recherche virale simple mais sans envoyer de fichiers contenant des informations sensibles puisque seulement les hashs sont envoyés. 

Le programme parcourt tous les fichiers inclus dans le dossier ainsi que les sous-dossiers passés en paramètre. Ensuite pour chacun d'eux, il va créer le hash MD5 du fichier puis envoyer la requête à VirusTotal pour faire une recherche dans leur base de données. Une fois la réponse reçue, si le résultat est positif, alors ce dernier est écrit dans un fichier comprenant son nom dans un dossier spécial.

![Résultat par fichier](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/TestVirusTotalRes.PNG)

De plus, dans un autre fichier corresponsant à l'analyse, celui-ci est écrit ainsi que le total de fichiers positifs sur le nombre de fichiers analysés.

![Ficheir de résultat général](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/TestVirusTotal.PNG)

Le script possède une fonction d'attente si le quota journalier sur l'API VirusTotal est atteint.

Il faut spécifier votre clé publique VirusTotal dans le code source.

![VirusTotal Logo](https://www.virustotal.com/ui-public/images/logo.svg)

## Analyse des fichiers

Un Nous avons créer un [script](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/AnalyseWord.py) qui permet de faire une analyse plus rapide des fichier DOCX. ce script ouvre uniquement les fichier qui ont moins de quatre paragraphe et dont le premier paragraphe fait moins de 40 caractere. Cela permet de faire un gros tris quand nous avons à  traiter des centaines de documents word. Une fois que le script a finit de travailler, des fichiers sont créés pour chaque résultat positif avec le texte des paragraphe dedans. Grâce à ce script nous avons juste à ouvrir les quelques fichier texte afin de vérifier leur contenu. 
Le script est différent pour Windows et Linux, car une bibliothèque n'est pas disponible sur Windows, le tout est transparent lors de l'utilisation, juste un petit message indique aux utilisateurs Windows la possiblité de fichier vide dans les résulats. 

Le script n'est pas écrit pour être sans failles mais plutôt pour avoir un tris efficace et rapide des fichiers Word. 
