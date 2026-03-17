# Troisième script à exécuter
# Attention au chemin hardcoder pour le répertoire et le parcours de fichier PDF dans le bas du fichier
from stegano import lsb
import os
import subprocess

# Fonction pour extraire les morceau des images
def extraire_morceau_de_image(image_chemin):
    code_cache = lsb.reveal(image_chemin)
    if code_cache:
        print(f"Extraction réussie depuis {image_chemin}")
        return code_cache
    else:
        print("Pas de code caché pour cette image")

# Fonction de reassemblage du script a partir des morceaux recupere
def reassembler_script(images, output_file):
    script_complet = ''
    for image in images:
        partie_script = extraire_morceau_de_image(image)
        print(f"Morceau extrait : \n\n{partie_script}\n\n")
        script_complet += partie_script

    with open(output_file, 'w') as file:
        file.write(script_complet)
    print(f"Script reconstruit sauvegardé sous : {output_file}")

# Recherche d'image dans le repertoire en parametre
def rechercher_images(repertoire):
    images_cachees = []
    for root, dirs, files in os.walk(repertoire):
        for file in files:
            if file.endswith(('.png', '.jpg')) and ('_idea' in file or '_maman' in file or '_toronto' in file):
                images_cachees.append(os.path.join(root, file))
    return images_cachees

# Execution du script reconstruit avec subprocess
def executer_script(script_chemin, chemin_demarage):
    try:
        subprocess.run(['python', script_chemin, chemin_demarage], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Erreur lors de l'exécution du script {script_chemin}: {e}")


repertoire = 'C:\\Users\\Utilisateur\\simulation'
images = rechercher_images(repertoire)

if images:
    reassembler_script(images, 'script_secret_reconstruit.py')

    chemin_pdf = 'C:\\Users\\Utilisateur\\Documents'
    executer_script('script_secret_reconstruit.py', chemin_pdf)