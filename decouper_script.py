# Fichier à exécuter en premier
# Découpe le fichier en entré en 3 fichiers texte
def decouper_script(fichier, parties=3):
    with open(fichier, 'r') as file:
        data = file.read()

    taille_partie = len(data) // parties

    for i in range(parties):
        debut = taille_partie * i

        if i < parties - 1:
            fin = taille_partie * (i + 1)
        else:
            fin = len(data)

        with open(f'partie_{i + 1}.txt', 'w') as partie:
            partie.write(data[debut:fin])

decouper_script('script_secret.py', 3)