# Analyse post-récupération 

## Analyse Virale

Le fichier VirusTotalAll permet d'analyser un dossier (passé en paramètre) en recherchant les hashs des fichiers du dossier sur [VirusTotal](https://www.virustotal.com/). Cela permet de faire une recherche virale simple mais sans envoyer de fichiers contenant des informations sensibles puisque seulement les hashs sont envoyés. 

Le programme parcourt tous les fichiers inclus dans le dossier ainsi que les sous-dossiers passés en paramètre. Ensuite pour chacun d'eux, il va créer le hash MD5 du fichier puis envoyer la requête à VirusTotal pour faire une recherche dans leur base de données. Une fois la réponse reçue, si le résultat est positif, alors ce dernier est écrit dans un fichier comprenant son nom dans un dossier spécial.

![Résultat par fichier](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/TestVirusTotalRes.PNG)

De plus, dans un autre fichier corresponsant à l'analyse, celui-ci est écrit ainsi que le total de fichiers positifs sur le nombre de fichiers analysés.

![Ficheir de résultat général](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/TestVirusTotal.PNG)

Le script possède une fonction d'attente si le quota journalier sur l'API VirusTotal est atteint.

Il faut spécifier la clé publique VirusTotal dans le code source.

![VirusTotal Logo](https://www.virustotal.com/ui-public/images/logo.svg)

## Analyse des fichiers

Nous avons créer un [script](https://github.com/hubos89/ProjectForensic/blob/master/Analyse%20post%20R%C3%A9cup%C3%A9ration/AnalyseWord.py) qui permet de faire une analyse plus rapide des fichiers DOCX. Ce script ouvre uniquement les fichiers qui ont moins de quatre paragraphes et dont le premier paragraphe fait moins de 40 caractères. Cela permet de dégrossir les quantités de données à trier car les documents Word que nous avons dû traiter se compte par centaines. Une fois que le script a fini de travailler, des fichiers sont créés pour chaque résultat positif contenant le texte sous forme de paragraphes. Ainsi ce script nous permet seulement d'ouvrir les quelques fichiers texte afin de vérifier leurs contenus. 

Le script contient des différences entre Windows et Linux car une bibliothèque n'est pas disponible sur Windows. Néanmoins, le tout est transparent lors de l'utilisation à la différence dans l'interface où un message indique aux utilisateurs Windows la possiblité d'existence de fichiers vides dans les résultats. 

Le script n'est pas écrit pour être sans faille mais plutôt pour avoir un tris efficace et rapide des fichiers Word. 
