import docx
import sys
import os 

if len(sys.argv) >=2 :#test si le parametre du dossier est bien donne
	for path, dirs, files in os.walk(sys.argv[1]):#parcours de dossier et sous dossier
		for filename in files:
			extension=filename.split('.')[-1] 
			if extension == "docx" :
				chemincomplet = path + "\\" + filename
				statinfo = os.stat(chemincomplet)
				if statinfo.st_size > 0 :
					document = docx.Document(chemincomplet)
					if len(document.paragraphs) < 3 :
						if len(document.paragraphs[0].text) < 41 :
							if not os.path.isdir(path + "\\potentielMDP\\") :
								os.mkdir(path + "\\potentielMDP\\")
							fichier = open(path + "\\potentielMDP\\" + filename + ".txt","a")
							fichier.write(document.paragraphs[0].text)
							if len(document.paragraphs) > 1 :
								fichier.write("\n"+document.paragraphs[1].text)
								if len(document.paragraphs) > 2 :
									fichier.write("\n"+document.paragraphs[2].text)
					
else : 
	print('\033[2;31;40m please give in parameter the directory to analyse.')
	print('\033[2;31;40m veuillez donner en parametre le dossier a analyser.')
