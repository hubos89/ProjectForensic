from __future__ import print_function
import sys
import shutil
import os
import json
import hashlib
from virus_total_apis import PublicApi as VirusTotalPublicApi
#test si le parametre du dossier est bien donne
if len(sys.argv) >=2 :
	compteurPositif = 0
	compteurTotal = 0
	#eneleve les fichiers d analyse precedent
	if os.path.isfile(sys.argv[1]+'resultats.txt'):
	        os.remove(sys.argv[1]+'resultats.txt')
	if not os.path.exists(sys.argv[1]+'res_positif/'):
	        os.mkdir(sys.argv[1]+'res_positif/')
        else :
                shutil.rmtree(sys.argv[1]+'res_positif/')
		os.mkdir(sys.argv[1]+'res_positif/')

	#fonction md5 pour grand fichier
	def md5(fname):
	    	hash_md5 = hashlib.md5()
    		with open(fname, "rb") as f:
        		for chunk in iter(lambda: f.read(4096), b""):
		            	hash_md5.update(chunk)
    		return hash_md5.hexdigest()
	#cle pour utiliser l api VirusTotal--------------------------------------------------------------------------------------------------------------------
	API_KEY = 'YourApiKey'
	#cle pour utiliser l api VirusTotal--------------------------------------------------------------------------------------------------------------------
	#parcours de dossier et sous dossier
	for path, dirs, files in os.walk(sys.argv[1]):
		for filename in files:
			compteurTotal = compteurTotal + 1
			MD5 = md5(path+'/'+filename)

			vt = VirusTotalPublicApi(API_KEY)
			response = vt.get_file_report(MD5)

			if response['results']['response_code'] == 1 : #si le hash est reconnu
				if response['results']['positives'] > 0 : #si le hash a une corespondance
					compteurPositif = compteurPositif + 1
					#ecrit le nom du fichier et le nombre de positif dans le fichier principal
					fichierGeneral = open(sys.argv[1]+'resultats.txt', "a")
					fichierGeneral.write(path+'/'+filename+' : '+str(response['results']['positives'])+'/'+str(response['results']['total'])+'\n')
					fichierGeneral.close()
					#ecrit le rapport dans un fichier propre au fichier
					fichierIndividuel = open(sys.argv[1]+'res_positif/'+filename+'.txt', "a")
					fichierIndividuel.write(json.dumps(response, sort_keys=False, indent=4))
					fichierIndividuel.close()
	# ecrit le nombre de positif a la fin du fichier
	fichierGeneral = open(sys.argv[1]+'resultats.txt', "a")
    fichierGeneral.write('\n'+' total : '+str(compteurPositif)+'/'+str(compteurTotal))
    fichierGeneral.close()
else : # si le chemin est pas donne affiche une erreur
	print('\033[2;31;40m please give in parameter the directory to analyse.')
	print('\033[2;31;40m veuillez donner en parametre le dossier a analyser.')
