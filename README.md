Benoita
=======

Benoita est un ouvrage écrit par Germaine Waton de Ferry (1885-1956), mon arrière-grand-mère.

Il est écrit en provencal et en français, chaque paragraphe trouvant sa traduction sur la page d'en face.

Mais il n'existe pas à ma connaissance de version numérique de ce livre.

Ce projet a donc plusieurs objectifs :
- réaliser la numérisation de l'ouvrage sous forme de fichiers image
- automatiser la reconnaissance de caractères sur l'ensemble des pages
- stocker informatiquement les textes récupérés, dans un format permettant de mettre en correspondance les contenus et leur traduction
- fournir un outil de visualisation, afin de pouvoir faire de la lecture comparée

## Pré-requis technique
- Python3 (disponible sur la plupart des plateformes)

## Installation
Dans une ligne de commande, taper
```
python3 -m venv venv
```
Cela aura pour effet de créer un environnement virtuel dans le dossier *venv*

Installer ensuite les paquets nécessaires avec cette commande
```
venv/bin/pip3 install -r requirements.txt
```

## Utilisation
La conversion depuis les scans situés dans le dossier __images/pages__ se fait avec cette commande
```
venv/bin/python3 ocr.py
```
On obtient en sortie des fichiers .hocr du même nom que les images fournies.

Vous pouvez ensuite les éditer avec n'importe quel éditeur de texte pour corriger les éventuelles erreurs de reconnaissance de caractères.

On peut enfin générer le PDF final (qui sera nommé out.pdf).
```
venv/bin/hocr-pdf output/ --savefile out.pdf
```

Note : un fichier out.txt sera également généré, contenant le texte intégral de toutes les pages.