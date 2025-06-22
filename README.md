Benoita
=======

Benoita est un ouvrage écrit par Germaine Waton de Ferry (1885-1956), mon arrière grand-mère.

Il est écrit en provencal et en français, chaque paragraphe trouvant sa traduction sur la page d'en face.

Mais il n'existe pas à ma connaissance de version numérique de ce livre.

Ce projet a donc plusieurs objectifs :
- réaliser la numérisation de l'ouvrage sous forme de fichiers image
- automatiser la reconnaissance de caractères sur l'ensemble des pages
- stocker informatiquement les textes récupérés, dans un format permettant de mettre en correspondance les contenus et leur traduction
- fournir un outil de visualisation, afin de pouvoir faire de la lecture comparée

## Pré-requis technique
- Python3 (disponible sur la plupart des plate-formes)

## Installation
Dans une ligne de commande, taper
```
python3 -m venv venv
```
cela aura pour effet de créer un environnement virtuel dans le dossier *venv*

Installer ensuite les paquets nécessaires avec cette commande
```
venv/bin/pip3 install -r requirements.txt
```

## Utilisation
La conversion depuis les scans situés dans le dossier __images__ se fait avec cette commande
```
venv/bin/python3 ocr.py
```