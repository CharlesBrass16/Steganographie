# Projet – Stéganographie et reconstruction de code

L’objectif était de dissimuler un script Python à l’intérieur d’images, puis de développer un outil capable de retrouver ces images, d’en extraire les données cachées, de reconstruire le script original et de l’exécuter.

---

## 1. decouper_script.py

Ce script a pour rôle de **préparer le code à dissimuler**.

Plus précisément, il :
- Prend en entrée un script Python (ex : `script_secret.py`)
- Le divise en plusieurs morceaux (au moins 3)
- Génère une série de fichiers texte (`partie_1.txt`, `partie_2.txt`, etc.)

Cette étape permet de fragmenter le code afin de rendre sa détection plus difficile une fois caché dans plusieurs images.

---

## 2. cacher_morceaux_dans_images.py

Ce script est responsable de la **dissimulation des morceaux de code dans des images**.

Fonctionnement :
- Associe chaque morceau de code à une image différente
- Utilise une technique de stéganographie pour intégrer les données dans l’image
- S’assure que l’image reste visuellement inchangée

Les images générées peuvent ensuite être dispersées dans un système de fichiers pour simuler un environnement réaliste.

---

## 3. extraire_et_executer.py

Ce script représente la partie la plus importante du projet : **la reconstruction du script caché**.

Il permet de :
- Parcourir une arborescence de dossiers (simulation d’un ordinateur utilisateur)
- Identifier les images contenant des données cachées
- Extraire les morceaux de code
- Réassembler le script original dans le bon ordre
- Exécuter automatiquement le script reconstruit

Cette étape simule un scénario d’analyse ou de récupération de code dissimulé.

---

## Objectif du projet

Ce projet met en évidence :
- Les techniques de **dissimulation de données (stéganographie)**
- Les risques liés à la **discrétion de code malveillant**
- Les défis associés à la **détection et à l’analyse de données cachées**

Il permet également de mieux comprendre comment certaines techniques peuvent être utilisées dans des contextes de cybersécurité, autant du point de vue offensif que défensif.

---

## Contenu du repository

- `decouper_script.py`
- `cacher_morceaux_dans_images.py`
- `extraire_et_executer.py`
- Fichiers images contenant les données cachées
- Fichiers intermédiaires générés



