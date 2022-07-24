---
layout: page
title: common/ar (français)
description: "Crée, modifie et extrais depuis des archives (`.a`, `.so`, `.o`)."
content_hash: 2ff4586f5ac2d87830e3ec78e57d0c8bdd560bc4
related_topics:
  - title: English version
    url: /en/common/ar.html
    icon: bi bi-globe
  - title: italiano version
    url: /it/common/ar.html
    icon: bi bi-globe
  - title: 한국어 version
    url: /ko/common/ar.html
    icon: bi bi-globe
  - title: 中文 version
    url: /zh/common/ar.html
    icon: bi bi-globe
---
# ar

Crée, modifie et extrais depuis des archives (`.a`, `.so`, `.o`).
Plus d'informations : <https://manned.org/ar>.

- Extrais tous les éléments depuis une archive :

`ar -x `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>

- Liste tous les éléments depuis une archive :

`ar -t `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>

- Remplace ou ajoute des fichiers à une archive :

`ar -r `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier2.o</span>

- Insère un fichier d'indexation (équivalent à `ranlib`) :

`ar -s `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>

- Crée une archive avec des fichiers et un fichier d'indexation qui l'accompagne :

`ar -rs `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/archive.a</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier1.o</span>` `<span class="tldr-var badge badge-pill bg-dark-lm bg-white-dm text-white-lm text-dark-dm font-weight-bold">chemin/vers/fichier2.o</span>
