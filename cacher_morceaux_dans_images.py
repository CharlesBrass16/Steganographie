# Fichier python à exécuter en deuxième
# Attention de faire attention au fichier image utilisé lors de l'appel de la fonction 'cacher'
from stegano import lsb
from PIL import Image

# À partir de 3 fichiers images de base, stocke les parties du script découpé par 'decouper_script.py' dans 3 nouvelles images
def cacher(image_chemin, texte_file, output_image):
    try:
        image = Image.open(image_chemin)

        with open(texte_file, 'r') as file:
            texte = file.read()

        image_stegano = lsb.hide(image, message=texte)

        if image_stegano:
            image_stegano.save(output_image)
            print(f"Image cachée sauvegardée sous : {output_image}")
        else:
            print(f"Erreur : Impossible de cacher le texte dans {image_chemin}")
    except Exception as e:
        print(f"Erreur lors de la sauvegarde de {output_image}: {e}")

cacher('maman.png', f'partie_{1}.txt', 'photo_maman.png')
cacher('toronto.png', f'partie_{2}.txt', 'voyage_toronto.png')
cacher('wallpaper.png', f'partie_{3}.txt', 'wallpaper_idea.png')